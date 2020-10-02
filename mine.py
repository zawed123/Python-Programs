#https://m.facebook.com/story.php?story_fbid=2841195876159241&id=100008065687908&refid=52&__tn__=-R
#Subscribed by Anaswara K

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

x,z=make_blobs(n_samples=250,centers=4,cluster_std=3,random_state=2)

sa=KMeans(n_clusters=5,max_iter=200)
pred_y = sa.fit_predict(x)
plt.scatter(x[:,0], x[:,1])
plt.scatter(sa.cluster_centers_[:, 0], sa.cluster_centers_[:, 1], s=300, c='red')
plt.show()
