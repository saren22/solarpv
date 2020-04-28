from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.CharField(max_length=50, primary_key=True)
    client_name = models.CharField(max_length=50)
    client_type = models.CharField(max_length=50)
    client_code = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name #returns client_name on shell output instead of object

class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    office_phone = models.CharField(max_length=50, null=True)
    cell_phone = models.CharField(max_length=50, null=True)
    prefix = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, on_delete = models.CASCADE)

class Location(models.Model):
    location_id = models.CharField(max_length=50, primary_key=True)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    postal_code = models.IntegerField(null=True)
    country = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    fax_number = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    client_id = models.ForeignKey(Client, on_delete = models.CASCADE)

class Test_Standard(models.Model):
    standard_id = models.CharField(max_length=50, primary_key=True)
    standard_name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, null=True)
    published_date = models.DateTimeField(null=True)

class Product(models.Model):
    model_number = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=50, null=True)
    cell_technology = models.CharField(max_length=50, null=True)
    cell_manufacturer = models.CharField(max_length=50, null=True)
    number_of_cells = models.IntegerField(null=True)
    number_of_cells_in_series = models.IntegerField(null=True)
    number_of_series_strings = models.CharField(max_length=50, null=True)
    number_of_diodes = models.IntegerField(null=True)
    product_length = models.CharField(max_length=50, null=True)
    product_width = models.CharField(max_length=50, null=True)
    product_weight = models.CharField(max_length=50, null=True)
    superstate_type = models.CharField(max_length=50, null=True)
    superstate_manufacturer = models.CharField(max_length=50, null=True)
    substrate_type = models.CharField(max_length=50, null=True)
    substrate_manufacturer = models.CharField(max_length=50, null=True)
    frame_type = models.CharField(max_length=50, null=True)
    frame_adhesive = models.CharField(max_length=50, null=True)
    encapsulate_type = models.CharField(max_length=50, null=True)
    encapsulant_manufacturer = models.CharField(max_length=50, null=True)
    junction_box_type = models.CharField(max_length=50, null=True)
    junction_box_manufacturer = models.CharField(max_length=50, null=True)

class Certificate(models.Model):
    certificate_number = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    report_number = models.CharField(max_length=50, null=True)
    issue_date = models.DateTimeField(null=True)
    standard_id = models.ForeignKey(Test_Standard, on_delete = models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete = models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete = models.CASCADE)


class Service(models.Model):
    service_id = models.CharField(max_length=50, primary_key=True)
    service_name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=100, null=True)
    is_fi_required = models.BooleanField()
    fi_frequency = models.CharField(max_length=50, null=True)
    standard_id = models.ForeignKey(Test_Standard, on_delete = models.CASCADE)

class Test_Sequence(models.Model):
    sequence_id = models.IntegerField(primary_key=True)
    sequence_name = models.CharField(max_length=50)

class Performance_data(models.Model):
    model_number = models.ForeignKey(Product, on_delete = models.CASCADE)
    sequence_id = models.ForeignKey(Test_Sequence, on_delete = models.CASCADE)
    max_system_voltage = models.CharField(max_length=50, null=True)
    voc = models.CharField(max_length=50, null=True)
    isc = models.CharField(max_length=50, null=True)
    vmp = models.CharField(max_length=50, null=True)
    imp = models.CharField(max_length=50, null=True)
    pmp = models.CharField(max_length=50, null=True)
    ff = models.CharField(max_length=50, null=True)





