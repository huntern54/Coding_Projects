from itertools import filterfalse

# tree node for inorder, preorder, postorder
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solutions: 

    # Contains Duplicate #217 (hash map)
    def containsDuplicate(self, nums):
        hashMap = {}

        for i, element in enumerate(nums):
            if element in hashMap:
                return True
            elif element not in hashMap:
                hashMap[element] = i 
        return False

    # Fibonacci Algorithm Recursively
    def fibonacci_Recursive(self, n):
        if n <= 0:
            return n
        elif n == 1: 
            return 1
        else:
            return self.fibonacci_Recursive(n-1) + self.fibonacci_Recursive(n-2)
    
    # Fibonacci Algorithm Iteratively
    def fibonacci_Iterative(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        fibStartPos0, fibStartPos1 = 0, 1
        
        # _ is indicating that the loop variable is not being used within the loop body. 
        # It is a convention to use _ as a variable name in such cases to indicate 
        # that the value is not important or relevant.
        for _ in range(2, n + 1 ):
            fibStartPos0, fibStartPos1 = fibStartPos1, fibStartPos0 + fibStartPos1

        return fibStartPos1
        
    # Two Sum #1 (hash maps)
    def twoSum(self, nums, target):

        hashMap = {}
         
        for i, element in enumerate(nums):
            PossibleTarget = target - element 
            if PossibleTarget in hashMap:
                return [hashMap[element], i]
            hashMap[element] = i

    # Valid Anagram #242 (two hash maps)
    def isAnagram(self, s, t):
        
        hashMapS, hashmMapT = {}, {} 

        if len(s) != len(t):
            return False 

        for i in range(len(s)):
            # if the hash key does not exist, you can use the get() to store the default key as 0
            # because it will throw a error if it is not already in the hash map
            hashMapS[s[i]] = 1 + hashMapS.get(s[i], 0)
            hashmMapT[s[i]] = 1 + hashmMapT.get(t[i], 0)

        for c in hashMapS:
            if hashMapS[c] != hashmMapT.get(c, 0):
                return False

        return True

    # Longest Palindrome Possible (set)
    def longestPalindrome(self, s):
        palindromeLetters = set()

        # check if empty "if not a string, return false"
        if not s: 
            return False 
        else: 
            for char in s: 
                # check if the char is in the string, if is, remove, if not add
                if char in palindromeLetters:
                    palindromeLetters.remove(char)
                else:
                    palindromeLetters.add(char)

            # Calculate the length of the longest palindrome
            # If there are remaining characters in the set, add 1 to the length
            if len(palindromeLetters) > 0:
                return len(s) - len(palindromeLetters) 
            else: 
                return len(s)

    # Valid Palindromes using Splicing (Array)
    def isPalindromeInArraySplicing(self, s):
        palindrome  = []

        for str in s: 
            if str == str[::-1]:
                palindrome.append(str)
        return palindrome

    # Valid Palindrome without Splicing (Array, two pointers)
    def isPalindromeInArrayWithoutSplicing(self, s):
        palindromeConfirmedArray  = []

        for word in s: 
            leftPointer, 
            rightPointer = 0, len(word) - 1
            isAPalindrome = True

            while leftPointer < rightPointer and isAPalindrome:
                if word[leftPointer] != word[rightPointer]:
                    isAPalindrome = False
                leftPointer += 1 
                rightPointer -= 1 

            if isAPalindrome:
                palindromeConfirmedArray.append(word)
                
        return palindromeConfirmedArray

    # Reverse a string (list manipulation and two pointers)
    def reverseString(self, s): 
        
        stringInReverseList = list(s) 
        leftPointer, rightPointer = 0, len(s) - 1

        while leftPointer < rightPointer:
            temp = stringInReverseList[leftPointer]
            stringInReverseList[leftPointer] = stringInReverseList[rightPointer]
            stringInReverseList[rightPointer] = temp
            leftPointer += 1 
            rightPointer -= 1 

        reversedString = ''.join(stringInReverseList)
        return reversedString

    # Reverese the strings in an array list (array, two pointers)
    def reverseStringInAListofStrings(self, stringList):
        
        reversedList = []

        for string in stringList:
            stringInReverseList = list(string) 
            leftPointer, rightPointer = 0, len(string) - 1

            while leftPointer < rightPointer:
                temp = stringInReverseList[leftPointer]
                stringInReverseList[leftPointer] = stringInReverseList[rightPointer]
                stringInReverseList[rightPointer] = temp
                leftPointer += 1 
                rightPointer -= 1 

            reversedString = ''.join(stringInReverseList)
            reversedList.append(reversedString)

        return reversedList

    # Tree Traversal In Order (left middle right)
    def inOrderTreeTraversal(self, node):
        if node:
            self.inOrderTreeTraversal(node.left)
            print(node.value, end=' ')
            self.inOrderTreeTraversal(node.right)

    # Tree Traversal Post Order (left right middle)
    def postOrderTreeTraversal(self, node):
         if node:
            self.postOrderTreeTraversal(node.left)
            self.postOrderTreeTraversal(node.right)
            print(node.value, end=' ')
    
    # Tree Traversal In Order (middle left right)
    def preOrderTreeTraversal(self, node):
         if node:
            print(node.value, end=' ')
            self.preOrderTreeTraversal(node.left)
            self.preOrderTreeTraversal(node.right)
    
    # Linked List Cycles (tortoise and hare)
    def LinkedListCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
    
    # Reverse a linked List 
    def reverseLinkedLists(self, head):
                
        # None <- head(prev) <- next(curr) -> next(temp) -> tail
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

    # Max Profit best time to sell stock (max function use)
    def bestTimeToBuyAndSellStocks(self, prices):
        leftPointer, rightPointer = 0, 1
        maxProf = 0 

        while rightPointer < len(prices):
            if prices[leftPointer] <= prices[rightPointer]:
                profit = prices[rightPointer] - prices[leftPointer]
                maxProf = max(maxProf, profit)
            elif prices[leftPointer] > prices[rightPointer]:
                leftPointer = rightPointer
            rightPointer += 1 
        return maxProf

def linkedListReversal():
    solution = Solutions()
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = solution.reverseLinkedLists(head)

    # Traverse and print the reversed linked list
    current = result
    while current: 
        print(current.val, end=" ")
        current = current.next

def doISell():
    solution = Solutions()
    prices = [7, 1, 5, 3, 6, 4]
    result = solution.bestTimeToBuyAndSellStocks(prices)
    print(result)

def tortoiseAndHare():
    solution = Solutions()
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # connection
    node5.next = node2

    result = solution.LinkedListCycle(head)
    print(result)
    
def treeTraversal():
    solution = Solutions()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Example tree          1
    #                     /    \
    #                   2        3
    #                 /   \    /   \
    #               4      5  6     7


    print("Inorder Traversal: ")
    solution.inOrderTreeTraversal(root)
    print()

    print("Preorder Traversal: ")
    solution.preOrderTreeTraversal(root)
    print()

    print("Postorder Traversal: ")
    solution.postOrderTreeTraversal(root)
    print()

def reverseAString():
    solution = Solutions()
    inputString = "Hello World!"
    stringList = ["Hellow World?", "Hi my name is Hunter", "This is a practice test"]
    result = solution.reverseString(inputString)
    resultList = solution.reverseStringInAListofStrings(stringList)
    print(result)
    print(resultList)
    
def palindromeInArray():
    solution = Solutions()
    inputString = ["level", "radar", "python", "madam", ":-1-13-:"]
    result = solution.isPalindromeInArraySplicing(inputString)
    result = solution.isPalindromeInArrayWithoutSplicing(inputString)
    print(result)

def longPalindromeOperation():
    solution = Solutions()
    inputString = "abccccdd"
    result = solution.longestPalindrome(inputString)
    print(result)

def ValidAnagram():
    callToIsAnagram = Solutions()
    s = ["anagram"]
    t = ["gramana"]
    result = callToIsAnagram.isAnagram(s, t)
    print(result)

def twoSumCall():
    solutionCall = Solutions()
    nums = [2,7,11,15]
    target = 9 
    result = solutionCall.twoSum(nums, target)
    print(result)

def containsDup():
    callToSolution = Solutions()
    testcase = [1,2,3,4,5]
    result = callToSolution.containsDuplicate(testcase)
    print(result)

def fibonacci():
    callToSolution = Solutions()
    fib_recur = callToSolution.fibonacci_Recursive(10)
    print(fib_recur)

    fib_iterative = callToSolution.fibonacci_Iterative(10)
    print(fib_iterative)

if __name__ == "__main__":
    # containsDup()
    # fibonacci()
    # twoSumCall()
    # ValidAnagram()
    # longPalindromeOperation()
    palindromeInArray()
    # reverseAString()
    # treeTraversal()
    # tortoiseAndHare()
    # doISell()
    # linkedListReversal()