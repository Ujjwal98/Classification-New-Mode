# Classification-New-Mode

1. Collect any dataset without decision attribute.

2.Let the dataset has m rows and n columns where, each row is an object and each column is an
attribute or feature of the object in the dataset. So you can consider the dataset as an m×n matrix.

3.Normalize the attribute values within the range [0, 1] using any normalization technique to give all
the attributes an equal importance.

4.Create a similarity matrix S of size m×m where, each (i, j)-th entry in the matrix gives the similarity
measurement between i-th and j-th objects. Use at least following similarity measures:
  i)Dice  ii)Jaccard  iii)Cosine  iv)Overlap
  
5.The i-th row indicates similarity of i-th object with all other objects. Find the average similarity of
i-th object with other objects and form a cluster Ci with i-th object and objects having similarity more
than the average similarity. Repeat this process for all rows of the similarity matrix. Thus, you have
now m clusters.

6.Remove the clusters (if any) which are subset of some other clusters. As a result you have now
say, p (< m) clusters.

7.Create a similarity matrix C of size p×p where, each (i, j)-th entry in the matrix gives the similarity
measurement between i-th cluster Ci and j-th cluster Cj using following similarity measure.

8.Out of all p2 entries in matrix C, find out the maximum value. If multiple maximum values occur,
choose any one randomly. Let, ckl is the maximum value selected, that implies clusters Ck and Cl are
the most similar clusters among all p clusters. Merge these two clusters Ck and Cl to get a new cluster
Ckl, i.e. Ckl = Ck∪ Cl.

9.Repeat steps 6 to 8 until desire number (say, at most K) of clusters are obtained.
