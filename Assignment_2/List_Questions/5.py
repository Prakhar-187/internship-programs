lis=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list=["h","i","j"]

print(lis[2][1][2][1])      #nested list/tuple/dictionary/set ko access ese krte h

# lis[2][1][2].insert(2 , ("h","i","j"))  #isse 1 position pr 1 hi aa paega vrna small braces k sath krte to small braces bh print ho jate
# print(lis[2][1][2].append(sub_list))     #isse pura sub list ek sath append ho jaega g k bad but [] nh hatenge 
print(lis[2][1][2].extend(sub_list))     #isse pura sub list k elements kitne bh ho sb ese k ese print ho jaenge but sirf last me without any braces

print(lis)
