require 'digest/md5'

def getMD5 (string)
    hash = Digest::MD5.hexdigest(string)
    return hash
end

def checkForSubStr (string, substring)
    pos = string.index(substring)
    if pos == 0
        return true
    end
    return false
end

input = "yzbqklnj"
start = 0

while true
    test = input + start.to_s
    hash = getMD5(test)
    # if checkForSubStr(hash, "00000")     this is for Part 1
    if checkForSubStr(hash, "000000")    # this is for Part 2
        puts hash
        puts test
        break
    end
    start += 1    
end