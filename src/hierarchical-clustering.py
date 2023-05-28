import time
import re
import json
import arxiv
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.feature_extraction.text import CountVectorizer
from fuzzywuzzy import fuzz

def read_faculty_names(filename):
    with open(filename, 'r') as file:
        faculty_names = file.read().splitlines()
    return faculty_names

def get_publications(faculty_names):
    filename = 'data/publications.json'

    try:
        print("Trying to load publications from file...")
        with open(filename, 'r') as file:
            print("Loading publications from file...")
            all_publications = json.load(file)
    except FileNotFoundError:
        print("File not found, fetching publications from arXiv...")
        all_publications = {}

        for name in faculty_names:
            print(f"Fetching publications for {name}")
            query = f"au:{name}"
            search = arxiv.Search(query=query, max_results=100)
            threshold = 95  # Start with a high threshold
            while threshold >= 80:  # Lower the threshold until it reaches 80
                for result in search.results():
                    for author in result.authors:
                        if fuzz.ratio(str(author), name) > threshold:
                            if name not in all_publications:
                                all_publications[name] = []
                            all_publications[name].append({'title': result.title, 'authors': [str(author) for author in result.authors], 'categories': result.categories})
                            break  # No need to check the other authors
                if name in all_publications and all_publications[name]:  # If any publications were found, break the loop
                    break
                else:  # If no publications were found, lower the threshold
                    threshold -= 5
            time.sleep(3)  # To prevent rate limiting

        print("Saving publications to file...")
        with open(filename, 'w') as file:
            json.dump(all_publications, file)

    return all_publications

def extract_tags(all_publications):

    faculty_tags = {}

    for faculty, publications in all_publications.items():
        print(f"Extracting tags for {faculty}")
        tags = []
        for publication in publications:
            # Regular expression to match arXiv taxonomy codes (e.g., math.PR or math.AT)
            regex = re.compile(r'\b[a-z]+(?:-?[a-z]+)?[.][A-Za-z]{2,}\b')
            extracted_tags = regex.findall(' '.join(publication['categories']))
            tags.extend(extracted_tags)
        faculty_tags[faculty] = tags

    return faculty_tags

faculty_names = read_faculty_names('data/names.txt')
all_publications = get_publications(faculty_names)
faculty_tags = extract_tags(all_publications)
with open('data/faculty_tags.json', 'w') as outfile:
    json.dump(faculty_tags, outfile)
# Convert the tags to a list of strings
tag_strings = [' '.join(tags) for tags in faculty_tags.values()]

# Create a binary matrix of tags
vectorizer = CountVectorizer(binary=True)
tag_matrix = vectorizer.fit_transform(tag_strings)

# Create a similarity matrix
similarity_matrix = pdist(tag_matrix.toarray(), metric='jaccard')

# Perform hierarchical clustering
Z = linkage(similarity_matrix, method='average')

# Cut the dendrogram
clusters = fcluster(Z, t=0.5, criterion='distance')

# Cut the dendrogram to create 10 clusters
#clusters = fcluster(Z, t=20, criterion='maxclust')

# Create a dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z, labels=faculty_names, orientation='left')
plt.title('Dendrogram')
plt.xlabel('distance')
plt.ylabel('faculty names')

# Save the figure to a file
plt.savefig('output/dendrogram.png', dpi=300)

# Close the figure
plt.close()



