# Generated by Django 4.2.6 on 2023-10-16 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_h1b_unitofpay'),
    ]

    operations = [
        migrations.AddField(
            model_name='h1b',
            name='AGENT_ATTORNEY_CITY',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='AGENT_ATTORNEY_NAME',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='AGENT_ATTORNEY_STATE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='CASE_NUMBER',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='CASE_STATUS',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='CASE_SUBMITTED',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='DECISION_DATE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_ADDRESS',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_CITY',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_COUNTRY',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_NAME',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_PHONE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_PHONE_EXT',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_POSTAL_CODE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_PROVINCE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYER_STATE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYMENT_END_DATE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='EMPLOYMENT_START_DATE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='FULL_TIME_POSITION',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='H_1B_DEPENDENT',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='JOB_TITLE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='NAIC_CODE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='ORIGINAL_CERT_DATE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='PW_SOURCE_OTHER',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='PW_SOURCE_YEAR',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='PW_WAGE_SOURCE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='SOC_CODE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='SOC_NAME',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='TOTAL_WORKERS',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='VISA_CLASS',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='WAGE_RATE_OF_PAY_FROM',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='WAGE_RATE_OF_PAY_TO',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='WAGE_UNIT_OF_PAY',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='WILLFUL_VIOLATOR',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='WORKSITE_CITY',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='WORKSITE_COUNTY',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='WORKSITE_POSTAL_CODE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='h1b',
            name='WORKSITE_STATE',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='h1b',
            name='unitofpay',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]