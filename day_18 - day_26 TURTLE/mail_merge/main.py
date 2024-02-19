PLACEHOLDER = "[name]"

with open("./input/names") as names:
    name_list = names.readlines()


def write_mail(mail_name: str):
    output_file = f"./output/{mail_name}_mail"

    with open(output_file, mode="w") as output:
        output.write(f"{new_letter}")


with open("./input/start_mail") as starting_mail:
    mail_template = starting_mail.read()

    for name in name_list:
        name = name.split('\n')[0]
        new_letter = mail_template.replace(PLACEHOLDER, name)
        write_mail(name)
