from js import document

def SKU_generator(*args, **kwargs):
    category = document.querySelector("#category").value
    product_name = document.querySelector("#product_name").value.strip()
    quantity = document.querySelector("#quantity").value

    if not product_name:
        document.querySelector("#sku_output").innerHTML = "<p class='text-danger'>Please enter a product name.</p>"
        return
    if not quantity:
        document.querySelector("#sku_output").innerHTML = "<p class='text-danger'>Please enter a valid stock quantity.</p>"
        return

    try:
        qty = int(quantity)
    except ValueError:
        document.querySelector("#sku_output").innerHTML = "<p class='text-danger'>Please enter a valid stock quantity.</p>"
        return

    if qty < 0:
        document.querySelector("#sku_output").innerHTML = "<p class='text-danger'>Please enter a valid stock quantity.</p>"
        return

    cat_abbr = category[:3].upper()
    name_abbr = ''.join(word[0].upper() for word in product_name.split() if word)[:3].ljust(3, 'X')
    qty_str = str(qty).zfill(3)

    sku = f"{cat_abbr}{name_abbr}{qty_str}"

    html = f"""
    <div class="result-box">
        <p class="mb-1">Generated SKU:</p>
        <p class="sku-code">{sku}</p>
        <small style="color: rgba(255,255,255,0.45);">
            Category: {category} | Product: {product_name} | Stock: {qty}
        </small>
    </div>
    """
    document.querySelector("#sku_output").innerHTML = html

def create_order(*args, **kwargs):
    items = []
    total = 0

    for i in range(1, 6):
        checkbox = document.querySelector(f"#item{i}")
        if checkbox.checked:
            price = int(checkbox.value)
            label = document.querySelector(f"#item{i}-label").textContent
            items.append((label, price))
            total += price

    if not items:
        document.querySelector("#show").innerHTML = "<p class='text-danger'>Please select at least one item.</p>"
        return

    receipt_lines = []
    for name, price in items:
        receipt_lines.append(f"<p class='mb-1'>{name}: \u20b1{price}</p>")
    receipt_html = "\n".join(receipt_lines)

    html = f"""
    <div class="result-box">
        <h5 class="mb-3">Order Receipt</h5>
        {receipt_html}
        <hr>
        <p class="receipt-total">Total: \u20b1{total}</p>
    </div>
    """
    document.querySelector("#show").innerHTML = html
