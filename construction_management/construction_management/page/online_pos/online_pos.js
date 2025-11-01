frappe.pages['online_pos'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: __('Animated Pro POS'),
        single_column: true
    });

    const orders_list = $('<div id="orders-list" style="display:flex; flex-wrap:wrap;"></div>').appendTo(page.main);
    $('<canvas id="salesChart" style="margin:20px 0; max-width:100%;"></canvas>').appendTo(page.main);

    let last_order_count = 0;

    function fetch_orders() {
        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Sales Order",
                filters: { docstatus: 1 },
                fields: ["name", "customer", "grand_total", "status", "delivery_date", "creation"]
            },
            callback: function(r) {
                if(r.message.length > last_order_count){
                    new Audio('/assets/secritaria/public/sounds/notification.mp3').play();
                }
                last_order_count = r.message.length;

                orders_list.empty();
                if(r.message) {
                    r.message.forEach(order => {
                        let intensity = Math.min(order.grand_total / 1000, 1);
                        let dynamicColor = `rgba(54, 162, 235, ${0.3 + 0.7*intensity})`;
                        let icon = order.status === "To Deliver" ? "🕒" :
                                   order.status === "Paid" ? "💵" :
                                   "✅";
                        let order_html = `
                            <div class="order-card" style="
                                border-radius:14px;
                                padding:16px;
                                margin:10px;
                                width:280px;
                                box-shadow: 2px 4px 16px rgba(0,0,0,0.25);
                                background:${dynamicColor};
                                color:#000;
                                transition: transform 0.4s, box-shadow 0.4s;
                                cursor:pointer;"
                                onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='4px 6px 20px rgba(0,0,0,0.35)';"
                                onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='2px 4px 16px rgba(0,0,0,0.25)';">
                                <h5>${icon} Order: ${order.name}</h5>
                                <p><strong>Customer:</strong> ${order.customer}</p>
                                <p><strong>Total:</strong> ${order.grand_total}</p>
                                <p><strong>Status:</strong> ${order.status}</p>
                                <p><strong>Delivery:</strong> ${order.delivery_date}</p>
                                <div style="margin-top:10px;">
                                    <button class="btn btn-primary btn-sm" onclick="create_invoice('${order.name}')">Invoice</button>
                                    <button class="btn btn-success btn-sm" onclick="pay_online('${order.name}', ${order.grand_total})">Pay Online</button>
                                    <button class="btn btn-warning btn-sm" onclick="mark_delivered('${order.name}')">Delivered</button>
                                </div>
                            </div>
                        `;
                        orders_list.append(order_html);
                    });

                    let labels = r.message.map(o => o.creation.substr(0,10));
                    let totals = r.message.map(o => o.grand_total);
                    const ctx = document.getElementById('salesChart').getContext('2d');
                    new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: labels,
                            datasets: [{
                                label: 'Daily Sales',
                                data: totals,
                                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                                borderColor: 'rgba(255, 99, 132, 1)',
                                borderWidth: 2,
                                fill: true,
                                tension: 0.4
                            }]
                        },
                        options: { responsive: true, plugins: { legend: { display: true }, tooltip: { enabled: true } } }
                    });
                }
            }
        });
    }

    fetch_orders();
    setInterval(fetch_orders, 15000);
};
