first_set={27,43,34}
second_set={34,93,22,27,43,53,48}

if(first_set.issubset(second_set)):
    print(f"First set is subset of second set: {True}")
    print(f"Second set is subset of first set: {False}")
else:
    print(f"First set is superset of second set: {False}")
    print(f"Second set is superset of first set: {True}")

if(first_set.issuperset(second_set)):
    print(f"First set is superset of second set: {True}")
    print(f"Second set is superset of first set: {False}")
else:
    print(f"First set is superset of first set: {False}")
    print(f"Second set is superset of second set: {True}")
    
if(first_set.issubset(second_set)):
    empty1=first_set.clear()
    print(f"First set: {first_set}")
else:
    empty2=second_set.clear()
    print(f"Second set: {second_set}")




