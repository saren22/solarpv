from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=50)
    client_type = models.CharField(max_length=50)
    client_code = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name #returns client_name on shell output instead of object

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)    
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, on_delete = models.CASCADE)

class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    fax_number = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, on_delete = models.CASCADE)

class Test_Standard(models.Model):
    standard_id = models.IntegerField(primary_key=True)
    standard_name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    published_date = models.DateTimeField()

class Product(models.Model):
    model_number = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    cell_technology = models.CharField(max_length=50)
    cell_manufacturer = models.CharField(max_length=50)
    number_of_cells = models.IntegerField()
    number_of_cells_in_series = models.IntegerField()
    number_of_series_strings = models.CharField(max_length=50)
    number_of_diodes = models.IntegerField()
    product_length = models.CharField(max_length=50)
    product_width = models.CharField(max_length=50)
    product_weight = models.CharField(max_length=50)
    superstate_type = models.CharField(max_length=50)
    superstate_manufacturer = models.CharField(max_length=50)
    substrate_type = models.CharField(max_length=50)
    substrate_manufacturer = models.CharField(max_length=50)
    frame_type = models.CharField(max_length=50)
    frame_adhesive = models.CharField(max_length=50)
    encapsulate_type = models.CharField(max_length=50)
    encapsulant_manufacturer = models.CharField(max_length=50)
    junction_box_type = models.CharField(max_length=50)
    junction_box_manufacturer = models.CharField(max_length=50)

class Certificate(models.Model):
    certificate_number = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    report_number = models.CharField(max_length=50)
    issue_date = models.DateTimeField()
    standard_id = models.ForeignKey(Test_Standard, on_delete = models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete = models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete = models.CASCADE)


class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    is_fi_required = models.BooleanField()
    fi_frequency = models.CharField(max_length=50)
    standard_id = models.ForeignKey(Test_Standard, on_delete = models.CASCADE)

class Test_Sequence(models.Model):
    sequence_id = models.IntegerField(primary_key=True)
    sequence_name = models.CharField(max_length=50)

class Performance_data(models.Model):
    model_number = models.ForeignKey(Product, on_delete = models.CASCADE)
    sequence_id = models.ForeignKey(Test_Sequence, on_delete = models.CASCADE)
    max_system_voltage = models.CharField(max_length=50)
    voc = models.CharField(max_length=50)
    isc = models.CharField(max_length=50)
    vmp = models.CharField(max_length=50)
    imp = models.CharField(max_length=50)
    pmp = models.CharField(max_length=50)
    ff = models.CharField(max_length=50)





