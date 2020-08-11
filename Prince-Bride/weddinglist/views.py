from django.shortcuts import render
from weddinglist.models import wedding_list
import decimal

# Create your views here.
def home_view(request, *args, **kwargs):  

    if request.method == "POST":
        # parse post submit values as index lists
        object = request.POST
        product_ids = object.getlist("product_id")
        product_names = object.getlist("product_name")
        product_brands = object.getlist("product_brand")
        product_prices = object.getlist("product_price")
        product_qty_ordereds = object.getlist("product_qty_ordered")
        product_payment_status = object.getlist("product_payment_status")

        # delete database list for user
        query_list = wedding_list.objects.filter(user_list=1)
        query_list.delete()

        # insert new rows into database
        a = 0
        max_items = len(product_ids)
        while a < max_items:
            wedding_list.objects.create(
                user_list = 1,
                product_id = int(product_ids[a]),
                product_name = product_names[a],
                product_brand = product_brands[a],
                product_price = float(product_prices[a].replace("GBP", "")),
                product_qty_ordered = float(product_qty_ordereds[a]),
                product_payment_status = product_payment_status[a]
            )
            a += 1
    query_list = wedding_list.objects.filter(user_list=1)
    html = ""
    a = 1
    for row in query_list:
        if row.product_payment_status == "Paid":
            styling = 'class="table-success"'
            payment_option = '<td>✔️</td>'
            remove_option = '<td></td>'
        else:
            styling = ''
            payment_option = '<td class="hover" onclick="purchase('+str(row.product_id)+','+str(row.product_qty_ordered)+');">💳</td>'
            remove_option = '<td class="hover" onclick="remove_row('+str(a)+');">❌</td>'
        cost = row.product_price * row.product_qty_ordered
        html = html + '<tr id="'+str(a)+'" '+styling+'>'
        html = html + '<td>'+str(a)+'</td>'
        html = html + '<td>'+row.product_name+'</td><input id="product_name_'+str(a)+'" style="display: none;" name="product_name" value="'+row.product_name+'">'
        html = html + '<td>'+row.product_brand+'</td><input id="product_brand_'+str(a)+'" style="display: none;" name="product_brand" value="'+row.product_brand+'">'
        html = html + '<td>'+str("%.2f" % row.product_price)+'GBP</td><input id="product_price_'+str(a)+'" style="display: none;" name="product_price" value="'+str(row.product_price)+'">'
        html = html + '<td>'+str("%.2f" % row.product_qty_ordered)+'</td><input id="product_qty_ordered_'+str(a)+'" style="display: none;" name="product_qty_ordered" value="'+str(row.product_qty_ordered)+'">'
        html = html + '<td>'+str("%.2f" % cost)+'GBP</td>'
        html = html + '<td>'+str(row.product_id)+'</td><input id="product_id_'+str(a)+'" style="display: none;" name="product_id" value="'+str(row.product_id)+'">'
        html = html + payment_option
        html = html + remove_option
        html = html + '<input id="product_payment_'+str(a)+'" style="display: none;" name="product_payment_status" value="'+row.product_payment_status+'">'
        html = html + '</tr>'

        a += 1
    parameters = {
        "my_list": html,
        "max_count": a
    }
    return render(request, "home.html", parameters)

def payment_view(request, *args, **kwargs):

    if request.method == "POST":
        object = request.POST
        cost = float(object.get("price").replace("GBP", "")) * float(object.get("quantity"))
        parameters = {
            "product_id": object.get("product_id"),
            "product_name": object.get("product_name"),
            "product_brand": object.get("product_brand"),
            "price": object.get("price"),
            "quantity": object.get("quantity"),
            "cost": str("%.2f" % cost)+"GBP"
        }
        return render(request, "payment.html", parameters)
    else:
        query_list = wedding_list.objects.filter(user_list=1)
        html = ""
        a = 1
        for row in query_list:
            if row.product_payment_status == "Paid":
                styling = 'class="table-success"'
                payment_option = '<td>✔️</td>'
                remove_option = '<td></td>'
            else:
                styling = ''
                payment_option = '<td class="hover" onclick="purchase('+str(row.product_id)+','+str(row.product_qty_ordered)+');">💳</td>'
                remove_option = '<td class="hover" onclick="remove_row('+str(a)+');">❌</td>'
            cost = row.product_price * row.product_qty_ordered
            html = html + '<tr id="'+str(a)+'" '+styling+'>'
            html = html + '<td>'+str(a)+'</td>'
            html = html + '<td>'+row.product_name+'</td><input id="product_name_'+str(a)+'" style="display: none;" name="product_name" value="'+row.product_name+'">'
            html = html + '<td>'+row.product_brand+'</td><input id="product_brand_'+str(a)+'" style="display: none;" name="product_brand" value="'+row.product_brand+'">'
            html = html + '<td>'+str("%.2f" % row.product_price)+'GBP</td><input id="product_price_'+str(a)+'" style="display: none;" name="product_price" value="'+str(row.product_price)+'">'
            html = html + '<td>'+str("%.2f" % row.product_qty_ordered)+'</td><input id="product_qty_ordered_'+str(a)+'" style="display: none;" name="product_qty_ordered" value="'+str(row.product_qty_ordered)+'">'
            html = html + '<td>'+str("%.2f" % cost)+'GBP</td>'
            html = html + '<td>'+str(row.product_id)+'</td><input id="product_id_'+str(a)+'" style="display: none;" name="product_id" value="'+str(row.product_id)+'">'
            html = html + payment_option
            html = html + remove_option
            html = html + '<input id="product_payment_'+str(a)+'" style="display: none;" name="product_payment_status" value="'+row.product_payment_status+'">'
            html = html + '</tr>'

            a += 1
        parameters = {
            "my_list": html,
            "max_count": a
        }
        return render(request, "home.html", parameters)

def payment_success_view(request, *args, **kwargs):

    if request.method == "POST":
        object = request.POST
        user_id = object.get("user_id")
        product_id = object.get("product_id")
        quantity = object.get("quantity")
        card_number = object.get("card")
        expiry = object.get("expiry_date")
        cvv = object.get("cvv")
        query_list = wedding_list.objects.filter(user_list=user_id, product_id=product_id, product_qty_ordered=quantity)
        # Update payment status of item
        query_list.update(product_payment_status="Paid")
        query_list = wedding_list.objects.filter(user_list=1)
        html = ""
        a = 1
        for row in query_list:
            if row.product_payment_status == "Paid":
                styling = 'class="table-success"'
                payment_option = '<td>✔️</td>'
                remove_option = '<td></td>'
            else:
                styling = ''
                payment_option = '<td class="hover" onclick="purchase('+str(row.product_id)+','+str(row.product_qty_ordered)+');">💳</td>'
                remove_option = '<td class="hover" onclick="remove_row('+str(a)+');">❌</td>'
            cost = row.product_price * row.product_qty_ordered
            html = html + '<tr id="'+str(a)+'" '+styling+'>'
            html = html + '<td>'+str(a)+'</td>'
            html = html + '<td>'+row.product_name+'</td><input id="product_name_'+str(a)+'" style="display: none;" name="product_name" value="'+row.product_name+'">'
            html = html + '<td>'+row.product_brand+'</td><input id="product_brand_'+str(a)+'" style="display: none;" name="product_brand" value="'+row.product_brand+'">'
            html = html + '<td>'+str("%.2f" % row.product_price)+'GBP</td><input id="product_price_'+str(a)+'" style="display: none;" name="product_price" value="'+str(row.product_price)+'">'
            html = html + '<td>'+str("%.2f" % row.product_qty_ordered)+'</td><input id="product_qty_ordered_'+str(a)+'" style="display: none;" name="product_qty_ordered" value="'+str(row.product_qty_ordered)+'">'
            html = html + '<td>'+str("%.2f" % cost)+'GBP</td>'
            html = html + '<td>'+str(row.product_id)+'</td><input id="product_id_'+str(a)+'" style="display: none;" name="product_id" value="'+str(row.product_id)+'">'
            html = html + payment_option
            html = html + remove_option
            html = html + '<input id="product_payment_'+str(a)+'" style="display: none;" name="product_payment_status" value="'+row.product_payment_status+'">'
            html = html + '</tr>'

            a += 1
        parameters = {
            "my_list": html,
            "max_count": a
        }
        return render(request, "home.html", parameters)
    else:
        query_list = wedding_list.objects.filter(user_list=1)
        html = ""
        a = 1
        for row in query_list:
            if row.product_payment_status == "Paid":
                styling = 'class="table-success"'
                payment_option = '<td>✔️</td>'
                remove_option = '<td></td>'
            else:
                styling = ''
                payment_option = '<td class="hover" onclick="purchase('+str(row.product_id)+','+str(row.product_qty_ordered)+');">💳</td>'
                remove_option = '<td class="hover" onclick="remove_row('+str(a)+');">❌</td>'
            cost = row.product_price * row.product_qty_ordered
            html = html + '<tr id="'+str(a)+'" '+styling+'>'
            html = html + '<td>'+str(a)+'</td>'
            html = html + '<td>'+row.product_name+'</td><input id="product_name_'+str(a)+'" style="display: none;" name="product_name" value="'+row.product_name+'">'
            html = html + '<td>'+row.product_brand+'</td><input id="product_brand_'+str(a)+'" style="display: none;" name="product_brand" value="'+row.product_brand+'">'
            html = html + '<td>'+str("%.2f" % row.product_price)+'GBP</td><input id="product_price_'+str(a)+'" style="display: none;" name="product_price" value="'+str(row.product_price)+'">'
            html = html + '<td>'+str("%.2f" % row.product_qty_ordered)+'</td><input id="product_qty_ordered_'+str(a)+'" style="display: none;" name="product_qty_ordered" value="'+str(row.product_qty_ordered)+'">'
            html = html + '<td>'+str("%.2f" % cost)+'GBP</td>'
            html = html + '<td>'+str(row.product_id)+'</td><input id="product_id_'+str(a)+'" style="display: none;" name="product_id" value="'+str(row.product_id)+'">'
            html = html + payment_option
            html = html + remove_option
            html = html + '<input id="product_payment_'+str(a)+'" style="display: none;" name="product_payment_status" value="'+row.product_payment_status+'">'
            html = html + '</tr>'

            a += 1
        parameters = {
            "my_list": html,
            "max_count": a
        }
        return render(request, "home.html", parameters)