
# Your Verkada security camera has added the ability to detect vehicles driving down the street using multiple cameras. The computer vision team can send you lists of vehicles that they have detected and they want to find out which vehicles have been detected by each camera.
#
# You are given a multi-dimensional array that contains arrays of integers. Each array represents all vehicles seen by each camera. Your task is to find out which vehicle identification codes were detected by all cameras.
#
# Examples:
#
# [[1, 3, 4, 8, 9, 16, 32, 40], [0, 1, 6, 7, 8, 12, 40, 62]]
# Output => [1, 8, 40]
#
# [[0, 19, 75, 111], [7, 19, 79, 101], [5, 6, 19]]
# Output -> [19]
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.array.integer input
#
# A sorted multi-dimensional array of integers between 0 and 1000.
#
# [output] array.integer
#
# Common elements in all arrays, sorted.


def vehicleDetection(input):
    totalDict = {}
    result = []
    for camera in input:
        for i in range(len(camera)):
            if camera[i] not in totalDict:
                totalDict[camera[i]] = 1
            else:
                totalDict[camera[i]] += 1
                if totalDict[camera[i]] == len(input):
                    result += [camera[i]]

    return result

# Your Verkada security camera has captured a funny video of a hummingbird. You'd like to post the clip on your social media account, but there were some people visible in the background. Since the image on a Verkada camera is so sharp and crisp, their faces are clearly identifiable, which you think might be an invasion of privacy. So you've decided to blur their faces before posting the clip
#
# You are given an image, represented as a matrix of integers, where each integer corresponds to a color. The number in the ith (0-based) row and jth (0-based) column represents the color of the pixel in the ith row and jth column of the image.
#
# Your task is to blur the image. In order to do that, you need to replace each number of the matrix with the average of the numbers in the neighboring cells. We assume that two cells are neighbors if they share at least one corner. The cell itself is not considered part of the average; only the 8 surrounding neighbors (or fewer if the cell is against an edge).
#
# Example
#
# For img = [[1, 4], [7, 10]], the output should be blurFaces(img) = [[7, 6], [5, 4]].
#
# newImg[0][0] = (4 + 7 + 10) / 3 = 21 / 3 = 7
# newImg[0][1] = (1 + 7 + 10) / 3 = 18 / 3 = 6
# newImg[1][0] = (1 + 4 + 10) / 3 = 15 / 3 = 5
# newImg[1][1] = (1 + 4 + 7) / 3 = 12 / 3 = 4
# For img = [[3, 0, 2, 5], [1, 2, 3, 4], [2, 3, 2, 3]], the output should be blurFaces(img) = [[1, 2.2, 2.8, 3], [2, 2, 2.625, 3], [2, 2, 3, 3]].
#
# newImg[0][0] = (0 + 1 + 2) / 3 = 3 / 3 = 1
# newImg[0][1] = (1 + 2 + 2 + 3 + 3) / 5 = 11 / 5 = 2.2
# newImg[0][2] = (0 + 2 + 3 + 4 + 5) / 5 = 14 / 5 = 2.8
# newImg[0][3] = (2 + 3 + 4) / 3 = 9 / 3 = 3
# newImg[1][0] = (0 + 2 + 2 + 3 + 3) / 5 = 10 / 5 = 2
# newImg[1][1] = (0 + 1 + 2 + 2 + 2 + 3 + 3 + 3) / 8 = 16 / 8 = 2
# newImg[1][2] = (0 + 2 + 2 + 2 + 3 + 3 + 4 + 5) / 8 = 21 / 8 = 2.625
# newImg[1][3] = (2 + 2 + 3 + 3 + 5) / 5 = 15 / 5 = 3
# newImg[2][0] = (1 + 2 + 3) / 3 = 6 / 3 = 2
# newImg[2][1] = (1 + 2 + 2 + 2 + 3) / 5 = 10 / 5 = 2
# newImg[2][2] = (2 + 3 + 3 + 3 + 4) / 5 = 15 / 5 = 3
# newImg[2][3] = (2 + 3 + 4) / 3 = 9 / 3 = 3
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.array.integer img
#
# A matrix of integers representing the colors of each pixel of the image.
#
# Guaranteed constraints:
# 1 ≤ img.length ≤ 50,
# 1 ≤ img[i].length ≤ 50,
# 0 ≤ img[i][j] ≤ 100.
#
# [output] array.array.float
#
# A matrix containing the colors of the resulting image. Your answer will be considered correct if for each matrix cell its absolute error doesn't exceed 10-5.


def blurFaces(img):
    continue



# Your Verkada security camera is part of your Enterprise IT Network. You're trying to debug an issue with your firewall, so you need to consult your data logs. You're mainly interested in seeing which devices are communicating with each other, so you'd like to find all the IP addresses within the logs.
#
# You have parsed your log files and found out that the log files are malformed. The IP addresses have been merged together and you need to find all possible IP addresses they could have been.
#
# Examples:
#
# "19216800" -> ["19.216.80.0","192.16.80.0","192.168.0.0"]
# "25525511135" -> [“255.255.11.135”, “255.255.111.35”]
# An IP address is a string of form x.x.x.x where each x is a number from 0 to 255. Each octet can not have leading zeros unless it is a 0.
#
# Your task is to find all distinct IP addresses from the input string and return them in an array in alphabetical order.
#
# [execution time limit] 4 seconds (py3)
#
# [input] string str
#
# String containing possible IP addresses.
#
# [output] array.string
#
# Array containing strings of IP addresses.


res = []
def restoreIpAddresses(s):
    helper(s, [], 0)
    return res


def helper(s, assignments, index):
    if len(assignments) == 4 and index == len(s): # 4 partitions and processed all char in s
        res.append(".".join(assignments))

    if len(assignments) > 4: # prune early
        return

    for i in range(index, min(index+3, len(s))):  # check from index to index + 3 or end of s
        if s[index] == '0' and i > index: # no leading 0 but allow single '0'
            continue
        if int(s[index:i+1]) <= 255: # if partition is valid, recurse
            helper(s, assignments + [s[index:i+1]], i + 1) # add partition and branch off to process next char
