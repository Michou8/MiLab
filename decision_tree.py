import numpy as np
from collections import Counter
def entropy(class_proba):
	return -np.dot(np.log(class_proba),class_proba)
print entropy(np.array([0.5,0.1,0.4]))

def proba_class(labels):
	total_count = len(labels)
	return [float(count)/total_count for count in Counter(labels).values()]
print proba_class(['','','k','o','o'])

def data_entropy(labels):
	proba = proba_class(labels)
	return entropy(proba)
print data_entropy(['','','k','o','o'])

def partition_entropy(subsets):
	total_count = sum([len(subset) for subset in subsets])
	return sum([data_entropy(subset)*len(subset) / total_count for subset in subsets])

print partition_entropy([['r','t'],['a','r','t'],['a','a','b']])

def partition_by(inputs_data,features_selected,label_field='label'):
	groups = {}
	for input in inputs_data:
		key = input[features_selected]
		if key not in groups:
			groups[key] = [input[label_field]]
		else:
			groups[key].append(input[label_field])
	return groups

input_data = [
{'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'no', "label": False},
{'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'yes', "label": False},
{'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'no', "label": True},
{'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'no', "label": True},
{'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'no', "label": True},
{'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'yes', "label": False},
{'level':'Mid', 'lang':'R', 'tweets':'yes', 'phd':'yes', "label": True},
{'level':'Senior', 'lang':'Python', 'tweets':'no', 'phd':'no', "label": False},
{'level':'Senior', 'lang':'R', 'tweets':'yes', 'phd':'no', "label": True},
{'level':'Junior', 'lang':'Python', 'tweets':'yes', 'phd':'no', "label": True},
{'level':'Senior', 'lang':'Python', 'tweets':'yes', 'phd':'yes', "label": True},
{'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'yes', "label": True},
{'level':'Mid', 'lang':'Java', 'tweets':'yes', 'phd':'no', "label": True},
{'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'yes', "label": False}
]
def partition_entropy_by(inputs_data,attribute):
	partitions = partition_by(inputs_data,attribute)
	return partition_entropy(partitions.values())

def entropy_selection(input_data,keys=['level','lang','tweets','phd']):
	for key in keys:
		print key,partition_entropy_by(input_data,key)
entropy_selection(input_data)

senior_inputs = [input for input in input_data if input['level']=="Junior"]
for key in ['lang','tweets','phd']:
	print key,partition_entropy_by(senior_inputs,key)
