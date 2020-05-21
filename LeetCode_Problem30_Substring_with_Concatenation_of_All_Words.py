# LeetCode Problem 30
# Difficulty - Hard

# Substring_with_Concatenation_of_All_Words

# Description
# You are given a string, s, and a list of words, words, that are all of the same length. 
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once 
# and without any intervening characters.
 
# Example 1:
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.

# Example 2:
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []



# Code

def findSubstring(self, s, words):
      """
      :type s: str
      :type words: List[str]
      :rtype: List[int]
      """

      # getting decriptive parameters
       
      word_length = len(words[0]) if len(words)>0 else 0
      no_of_words = len(words)
      total_word_length = word_length*no_of_words
      total_string_length = len(s)

      result = []
      
      # return blank if s is blank or words is blank or s < total words
      if total_string_length<total_word_length or total_word_length==0 or total_string_length==0:
          return result

      word_dict = {}
      
      # creating a dictionary for individual word counts
      
      for word in words :
          if(word in word_dict):
              word_dict[word] += 1
          else:
              word_dict[word] = 1


      for i in range(0,(total_string_length-total_word_length+1)):
          
          # iterating over s and obtaining substring
          word_compare = s[i:(i+total_word_length)]

          #word_list = [word_compare[i:i+word_length] for i in range(0,                                                                           len(word_compare),word_length)]
          check_word_dict = word_dict.copy()

          j=0
          while j<total_word_length:
              # getting word chunks in substring iteration word_compare
              word = word_compare[j:j+word_length]
              if word in check_word_dict.keys():
                  check_word_dict[word]-=1    # reducing word count to finally check if exact match
              else:
                  break
              j+=word_length

          if max(check_word_dict.values())==0:
              result.append(i)

      return result
