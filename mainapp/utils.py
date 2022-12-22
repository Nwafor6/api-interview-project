from uuid import uuid4

def generate_random_id(length=5):
	random_id = str(uuid4())
	print(random_id)
	return random_id[:length]


def id_without_hyhen():

	main_id=""
	id=str(uuid4())
	for i in id:
		if i != "-":
			main_id += i
	print(main_id)
	return main_id

id_without_hyhen()
generate_random_id()
