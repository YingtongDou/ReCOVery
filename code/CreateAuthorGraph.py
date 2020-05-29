import networkx
import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from netwulf import visualize


def get_list_authors(authors):
    # First 3 lines convert string to list. list_auth is the final list of authors
    string_auth = authors[1:len(authors) - 1]
    string_auth = string_auth.strip()
    string_auth = string_auth.replace('\'', '')
    list_auth = string_auth.split(",")
    return list_auth


df = pd.read_csv("../dataset/recovery-news-data.csv")
authors = df['author'].dropna().unique()
G=networkx.Graph()

all_authors=[]
count=0
for author in authors:
    all_authors.append(get_list_authors(author))
del all_authors[3]

authors_list = []
list_auth_dict = []
for author in all_authors:
    #print(author)
    num_auth_dict = {}
    for each_author in author:
        each_author = each_author.strip()
        if each_author not in authors_list:
            authors_list.append(each_author)
            count+=1
            num_auth_dict[count] = each_author
        else:
            print(authors_list.index(each_author), each_author)
            num_auth_dict[authors_list.index(each_author)+1] = each_author
    list_auth_dict.append(num_auth_dict)

print(list_auth_dict)
# print(authors_list)

#     #print(list_author)
#     flag=False
#     num_auth = {}
#     multiple_authors = []
#     for index, each_author in enumerate(list_author):
#         if each_author not in num_auth:
#             flag = True
#             count+=1
#             num_auth[count] = each_author
#
#     if flag == True:
#         all_authors.append(num_auth)
#
# print(all_authors)

for authors1 in list_auth_dict:
    keys_array = []
    for key in authors1.keys():
        keys_array.append(key)
        G.add_node(key)
    #print(keys_array)

    if len(authors1) > 1:
        pairs = list(itertools.combinations(keys_array, 2))
        #print(pairs)
        for pair in pairs:
            G.add_edge(pair[0],pair[1])


#Display the graph
degrees = networkx.degree(G)
pos = networkx.spring_layout(G,k=0.20,iterations=30, scale=200)
# pos = networkx.spectral_layout(G, weight="weight", scale=200)

for degree in degrees:
    if degree[1] == 0:
        networkx.draw_networkx_nodes(G, pos, node_color='black', nodelist=[degree[0]], node_size=10,alpha=1)
    elif degree[1] == 1:
        networkx.draw_networkx_nodes(G, pos, node_color='purple', nodelist=[degree[0]], node_size=40, alpha=1)

    elif degree[1] == 2:
        networkx.draw_networkx_nodes(G, pos, node_color='orange', nodelist=[degree[0]], node_size=80, alpha=1)

    elif degree[1] == 3:
        networkx.draw_networkx_nodes(G, pos, node_color='green', nodelist=[degree[0]], node_size=120, alpha=1)
    else:
        networkx.draw_networkx_nodes(G, pos=pos, node_color='red', nodelist=[degree[0]], node_size=160, alpha=1)

#networkx.draw_networkx_nodes(G,pos,node_color='black',node_size = 50, alpha=0.8)
#networkx.draw_networkx_edges(G,pos,width=2.0,edge_color='b', alpha=0.8)
# networkx.draw(G, with_labels=False, node_size = 10, weight=10, pos=pos)
#
# plt.draw()
# plt.show()

visualize(G)














    #for key

    # pairs = list(itertools.combinations(range(len(indexes)), 2))
    # if len(pairs) == 0:
    #     pairs = indexes
    # for pair in pairs:
    #     #print(pair)
    #     if type(pair) != int:
    #         G.add_edge(pair[0], pair[1])

#
#     if len(pairs) == 0:
#         pairs = indexes
#
#     pairs_list = np.array([])
#     for pair in pairs:
#         if type(pair) != int:
#             pairs_list = np.append(pairs_list, np.asarray(list(pair)))
#         else:
#             pairs_list = np.append(pairs_list, np.asarray(pair))
#     #pairs_list = np.asarray(pairs_list)
#     all_authors = np.append(all_authors,(pairs_list))
#
# npa = np.asarray(all_authors)
#
# A = np.array([[1, 1], [2, 1]])
#
# print(A)
# print(npa.shape)
# # G = networkx.nx.from_numpy_array(all_authors)
# # G.edges(data=True)

# networkx.draw(G, with_labels=False)
# plt.draw()
# plt.show()




