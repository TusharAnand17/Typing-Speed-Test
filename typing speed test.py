import time
import random
import os

sentences_list = ["The quick brown fox jumps over the lazy dog", "A bird in the hand is worth two in the bush", "Caught between a rock and a hard place", "Closing the barn door after the horse escapes", "lease take your dog, Cali, out for a walk – he really needs some exercise!", "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine",
                  "Max Joykner sneakily drove his car around every corner looking for his dog", "We climbed to the top of the mountain in just under two hours; isn’t that great?", "here are so many places to go in Europe for a vacation--Paris, Rome, Prague, etc", "Your car is out of date as soon as it is paid for"]


i = 5
while (i):
    try:
        print("\n\n\t\t\t\t\t\tTyping Speed Test")
        org_sen = random.choice(sentences_list)
        sentences_list.remove(org_sen)
        org_word = org_sen.split(' ')
        word_count_org = len(org_word)
        print(org_sen)
        start_time = time.time()
        typed_sen = input("Type Here>> ")
        end_time = time.time()
        time_duration = end_time-start_time
        typed_word = typed_sen.split(' ')
        count = 0
        for x, y in zip(org_word, typed_word):
            if x == y:
                count += 1

        if count == word_count_org:
            acc_ = 100
        else:
            acc_ = (count/word_count_org)*100

        wpm_ = (count/time_duration)*60

        i -= 1

        credit = ""
        if acc_ > 85:
            credit = "Wow your accuracy is Good....Keep it Up"
            print(f"\n{credit}\nWPM: {wpm_} Accuracy: {acc_} Time Consumed: {time_duration}")

        else:
            credit = "Keep Practicing to Improve your accuracy"
            print(f"\n{credit}\nWPM: {wpm_} Accuracy: {acc_} Time Consumed: {time_duration}")

        time.sleep(4)
        os.system('cls')

    except Exception as e:
        print(e)

        os.system('cls')