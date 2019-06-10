import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    #print(kernel.respond(input("Enter your message >> ")))
    #ans_form_dataset = kernel.respond(input("Enter your message >> "))

    user_message = input("Enter your message >> ")
    sem = {'sem-1':'sem1', 'sem-2':'sem2', 'sem-3':'sem3', 'sem-4':'sem4'}
    department = ['Computer', 'IT', 'Electronics', 'Electrical', 'Mechanical', 'Civil', 'Production', 'EC']

    user_message_list = user_message.split(" ")
    print(user_message_list)

    for msg in user_message_list:
        if msg in department:
            dept_response = msg
        if msg in sem:
            sem_response = sem[msg]

    #print(find_response)
    print(dept_response)
    print(sem_response)
    find_response = dept_response + " " + sem_response
    kernel_response = kernel.respond(find_response)

    if '//' in kernel_response:
    	print("URL")
    else:
    	print("Not URL")