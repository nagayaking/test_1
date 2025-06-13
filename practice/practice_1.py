scores =  {"数学":82,"国語":74,"英語":60,
           "理科":92,"社会":70}

#理科と社会の点数の差を表示
score_science = scores["理科"]
score_society = scores["社会"]

print(f"{score_science-score_society}点")

#五教科の平均点を表示
ave = sum(list(scores.values()))/len(scores)

print(f"{ave}点")