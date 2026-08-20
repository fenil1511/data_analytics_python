user = [1,'fenil','fenil@gmail.com']
profile =[1,'adult','kids']
view=[100,20,50,60,30,20,10]

# nested_list
# x = [1,'fenil','fenil@gmail.com',[1,'adult','kids']]


#count => used to count how many time value is repeat heare fenil repet 2 time 
# print(user.count('fenil'))  

#index => it return index value of give value here fenil index is 1 
# print(user.index('fenil',2))

#insert => it use to insert values in list 
# insert_value_in_user = user.insert(2,'python')

# pop_value_in_user = user.pop()
# pop => remove the value from the list if we don't give the index it remove last value bydefault
# pop_value_in_user = user.pop()

#extend => merge two lists 
# user.extend(profile)

# copy is use to copy list of all elements and create nwe list 
# netflix=user.copy()
# netflix=user[:]
# print(netflix)

# sort use to asc or dsc the list by revrese= true or false 
# list3=view.sort(reverse=True)

# top_three = view[:5]
# top_two = view[-2:]

# total_view = sum(view)
# max_view = max(view)
# min_view = min(view)
# len_of_view = len(view)
# Built-in Data Functions

# add element in last
# user.append('jay')

# remove 
# user.remove('fenil@gmail.com')

high_view = [v for v  in view if v > 30 ]
print(high_view)