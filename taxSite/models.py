from django.db import models

# Create your models here.


class Prove(models.Model):
    tax_prove_num = models.CharField(max_length=32)
    taxpayer_name = models.CharField(max_length=32)
    issuing_date = models.DateField()
    taxpayer_id = models.IntegerField()


class List(models.Model):
    print_date = models.DateField()
    check_code = models.CharField(max_length=32)
    taxpayer_name = models.CharField(max_length=32)
    taxpayer_idCard_num = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.taxpayer_name, self.taxpayer_idCard_num, self.check_code, self.print_date


class ListItem(models.Model):
    tax_prove_num = models.ForeignKey(List, on_delete=models.CASCADE)
    tax_tag = models.CharField(max_length=32, default='工资薪金所得')
    declaration_date = models.DateField()
    declaration_income = models.FloatField()
    paid_up_tax_amount = models.FloatField()
    tax_start_time = models.DateField()
    tax_end_time = models.DateField()

    def __str__(self):
        return self.tax_tag

    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    '''