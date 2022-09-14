def lev_dist(word1, word2):

   n = len(word1)

   m = len(word2)

   if n == 0 or m == 0:

       return max(n, m)

   else:

       if word1[n] == word[m]:

           return lev_dist(word1[:n], word2[:m])

       else:

           return 1 + min(lev_dist(word1, word2[:m]),

                                   lev_dist(word1[:n], word2),

                                   lev_dist(word1[:n], word[:m]))

