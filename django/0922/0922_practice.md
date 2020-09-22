# 0922_practice



13 . q = User.objects.filter(phone__startswith ='010')

​		q.values('country').distinct()