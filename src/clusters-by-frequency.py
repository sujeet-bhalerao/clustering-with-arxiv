import time
import re
import json
import arxiv
from collections import Counter
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
            threshold = 95  
            while threshold >= 80:  
                for result in search.results():
                    for author in result.authors:
                        if fuzz.ratio(str(author), name) > threshold:
                            if name not in all_publications:
                                all_publications[name] = []
                            all_publications[name].append({'title': result.title, 'authors': [str(author) for author in result.authors], 'categories': result.categories})
                            break 
                if name in all_publications and all_publications[name]:  
                    break
                else:  
                    threshold -= 5
            time.sleep(3)  

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

"""def jaccard_similarity(list1, list2):
s1 = set(list1)
s2 = set(list2)
return len(s1.intersection(s2)) / len(s1.union(s2))
"""

def assign_to_most_frequent_cluster(faculty_tags):
    faculty_clusters = {}

    def add_to_cluster(name, tag):
        if tag not in faculty_clusters:
            faculty_clusters[tag] = []
        faculty_clusters[tag].append(name)

    for name, tags in faculty_tags.items():
        most_common_tag = Counter(tags).most_common(1)[0][0]
        add_to_cluster(name, most_common_tag)

    single_member_clusters = [tag for tag, members in faculty_clusters.items() if len(members) == 1]
    
    for tag in single_member_clusters:
        lone_member = faculty_clusters[tag][0]

        sorted_tags = [t for t, _ in Counter(faculty_tags[lone_member]).most_common()]
        next_tags = sorted_tags[1:]

        for next_tag in next_tags:
            if next_tag in faculty_clusters and next_tag != tag:  
                add_to_cluster(lone_member, next_tag)
                faculty_clusters[tag].remove(lone_member)
                break


    faculty_clusters = {tag: members for tag, members in faculty_clusters.items() if members}

    return faculty_clusters

faculty_clusters = assign_to_most_frequent_cluster(faculty_tags)

for tag, cluster in faculty_clusters.items():
    print(f"Cluster {tag}:")
    print(', '.join(cluster))
    print()


