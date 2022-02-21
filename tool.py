import csv
if __name__ == '__main__':

# Loading the sample.csv as LIST 
	with open('customer_sample.csv', 'r', encoding='utf8') as f:
		sample = f.read()
		sample_list = list(sample.split())
		sample_list = sample_list[1:]
		

# Loading the customer.csv file as DICTIONARY
	with open('customer.csv', 'r', encoding='utf8') as csvfile:
		customers = csv.reader(csvfile)
		customers_list = list(customers)
		fields_customer = customers_list[0]
		customers_list = customers_list[1:]
		
	customers_dict = {}
	for lst in customers_list:
		code = lst.pop(0)
		customers_dict[code] = lst 

# Loading the invoice.csv as DICTIONARY
	with open('invoice.csv', newline='', encoding='utf8') as csvfile:
		invoice = csv.reader(csvfile)
		invoice_list = list(invoice)
		fields_invoice = invoice_list[0]
		invoice_list = invoice_list[1:]

	invoice_dict = {}
	for lst in invoice_list:
		code = lst.pop(0)
		if code in invoice_dict.keys():
			invoice_dict[code] = invoice_dict[code]+ [lst]
		else:
			invoice_dict[code] = [lst]



# Loading the invoid_item.csv as DICTIONARY
	with open('invoice_item.csv', newline='', encoding='utf8') as csvfile:
		invoice_item = csv.reader(csvfile)
		invoice_item_list = list(invoice_item)
		invoice_item_list = invoice_item_list[1:]

	invoice_item_dict = {}
	for lst in invoice_item_list:
		code = lst.pop(0)
		if code in invoice_item_dict.keys():
			invoice_item_dict[code] = invoice_item_dict[code]+ [lst]
		else:
			invoice_item_dict[code] = [lst]
	


# CREATING THE NEW FILES
	new_customers_list = []
	new_invoice_list = []
	new_invoice_item_list = []

	for customer in sample_list:
		customer_info = [customer] + customers_dict[customer]
		new_customers_list.append(', '.join(customer_info))

		customer_invoice = invoice_dict[customer] #invoice = [inv code, amount, date]
		for detail_list in customer_invoice: 
			# print(detail_list)
			full_invoice = [customer] + detail_list # [cust code, inv code, amount, date]
			# print(full_invoice)
			new_invoice_list.append(', '.join(full_invoice))

		for inv_list in customer_invoice:
			inv_code = inv_list[0]
			inv_items_list = invoice_item_dict[inv_code]

			for item in inv_items_list:
				item_name = item[0]
				amount = item[1]
				quantity = item[2]
				new_invoice_item_list.append(', '.join([inv_code,item_name,amount,quantity]))

	

# SPLITING THE STRINGS - CUST
	new_customers = []
	for c in new_customers_list:
		splited_cus = c.split(',')
		new_customers.append(splited_cus)

# SPLITTING THE STRINGS - INVOICE
	new_invoice = []
	for inv in new_invoice_list:
		splited_inv = inv.split(',')
		new_invoice.append(splited_inv)
	
# SPLITTING THE STRINGS - INV ITEM
	new_items = []
	for inv in new_invoice_item_list:
		splited_inv = inv.split(',')
		new_items.append(splited_inv)




# WRITING THE FILES
	with open('new_customers.csv', 'w', newline = "") as f:
		fieldnames = ['“CUSTOMER_CODE”','“FIRSTNAME”','“LASTNAME”']
		writer = csv.DictWriter(f, fieldnames = fieldnames)
		writer.writeheader()
		for c in new_customers:
			writer.writerow({'“CUSTOMER_CODE”':c[0], '“FIRSTNAME”':c[1], '“LASTNAME”':c[2]})


	with open('new_invoice.csv', 'w', newline = "") as f:
		fieldnames = ['“CUSTOMER_CODE”' ,'“INVOICE_CODE”','“AMOUNT”','“DATE”']
		writer = csv.DictWriter(f, fieldnames = fieldnames)
		writer.writeheader()
		for inv in new_invoice:
			writer.writerow({'“CUSTOMER_CODE”':inv[0], '“INVOICE_CODE”':inv[1], '“AMOUNT”':inv[2], '“DATE”':inv[3]})

	with open('new_items.csv', 'w', newline = "") as f:
		fieldnames = ['“INVOICE_CODE”' ,'“ITEM_CODE”','“AMOUNT”','“QUANTITY”']
		writer = csv.DictWriter(f, fieldnames = fieldnames)
		writer.writeheader()
		for inv in new_items:
			writer.writerow({'“INVOICE_CODE”': inv[0], '“ITEM_CODE”': inv[1], '“AMOUNT”': inv[2], '“QUANTITY”': inv[3]})


