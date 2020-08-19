from celery import shared_task


@shared_task
def sample_task():
    print("The sample task just ran.")
    return 'Pokus The sample task just ran.'


@shared_task
def export_pohoda_adresy_add():
    print("Export adres do pohody ran.")
    # call_command("email_report", )
