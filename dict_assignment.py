# 1
def get_total_population(population):
	total_pop = 0
	num_cities = 0
	for key, val in population.items():
		total_pop += val
		num_cities += + 1
	#print (f"The total population of all {num_cities} cities is {total_pop}.")
	return (f"The total population of the cities is: {total_pop}")
    

# 2   
def get_large_city_count(population):
	num_large_cities = 0
	for key, val in population.items():
		if val > 1000000:
			num_large_cities += +1
		else:
			continue
	#print(f"There are {num_large_cities} with a population over 1 million")
	return (f"The number of cities over one million population are: {num_large_cities}")

  


# 3   
def get_num_cities_larger_than(population,):
	num_larger_cities = 0
	for key, val in population.items():
		if val > 700000:
			num_larger_cities += +1
		else:
			continue
	#print(f"There are {num_large_cities} with a population over 700k")
	return (f"The number of cities with population over 700K are: {num_larger_cities}")
	
	
    
# 4   
def get_largest_city(population):
	largest_pop = 0
	largest_city = ""
	for key, val in population.items():
		if largest_pop < val:
			largest_pop = val
			largest_city = key
		else:
			continue
	#print (f"The largest city is {largest_city} with a population of {largest_pop}")
	return (f"The largest city in population is: {largest_city}")
# 5   
def get_smallest_city(population):
	smallest_pop = float("inf")
	smallest_city = ""
	for key, val in population.items():
		if smallest_pop > val:
			smallest_pop = val
			smallest_city = key
		else:
			continue
	#print (f"The smallest city is {smallest_city} with a population of {smallest_pop}")
	return (f"The smallest city in population is: {smallest_city}")
    

def main():
	us_city_population = { 'Los Angeles': 3967000, 'Baltimore': 609032, 
						  'Denver': 705576, 'Chicago': 2710000, }
	print(get_total_population(us_city_population))
	print(get_large_city_count(us_city_population))
	print(get_num_cities_larger_than(us_city_population))
	print(get_largest_city(us_city_population))
	print(get_smallest_city(us_city_population))
	
if __name__ == '__main__':
	main()

