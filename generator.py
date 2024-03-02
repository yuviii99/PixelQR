import segno
import uuid
import os


def generate_qr(file_path, event_name, qr_uuid_list):
    for uuid in qr_uuid_list:
        qr_code = segno.make_qr(uuid)
        qr_code.save(f"{file_path}/{event_name}/{uuid}.png")


def generateUUID(event_name):
    id = uuid.uuid4()
    print(type(id))
    return event_name + "-" + str(id)


if __name__ == '__main__':
    event_name = input("Enter the number of event: ").strip().replace(" ", "_")
    qr_quantity = int(input("Enter the number of QR you want to generate: "))
    qr_uuid_list = []
    for i in range(qr_quantity):
        qr_uuid_list.append(generateUUID(event_name))
    os.makedirs(f"qr_codes/{event_name}")
    generate_qr(os.getcwd() + "/qr_codes", event_name, qr_uuid_list)
