sample_list=[11,45,8,23,14,12,78,45,89]
print(f"Original list: {sample_list}")

chunk_1=sample_list[0:3]
print(f"Chunk 1: {chunk_1}")
rev1=sample_list[-7:-10:-1]
print(f"After reversing it: {rev1}")

chunk_2=sample_list[3:6]
print(f"Chunk 2: {chunk_2}")
rev2=sample_list[-4:-7:-1]
print(f"After reversing it: {rev2}")

chunk_3=sample_list[6:9]
print(f"Chunk 3: {chunk_3}")
rev3=sample_list[-1:-4:-1]
print(f"After reversing it: {rev3}")