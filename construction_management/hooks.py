app_name = "construction_management"
app_title = "Construction Management"
app_publisher = "waddah"
app_description = "Construction Management"
app_email = "wd@wd.wd"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/construction_management/css/construction_management.css"
# app_include_js = "/assets/construction_management/js/construction_management.js"
app_include_js = "/assets/construction_management/js/material_request.js"

# include js, css files in header of web template
# web_include_css = "/assets/construction_management/css/construction_management.css"
# web_include_js = "/assets/construction_management/js/construction_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "construction_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "construction_management/public/icons.svg"


override_doctype_dashboards = {
	"Task": "construction_management.construction_management.overrides.task_dashboard.custom_get_dashboard_data"
}




# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "construction_management.utils.jinja_methods",
# 	"filters": "construction_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "construction_management.install.before_install"
# after_install = "construction_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "construction_management.uninstall.before_uninstall"
# after_uninstall = "construction_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "construction_management.utils.before_app_install"
# after_app_install = "construction_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "construction_management.utils.before_app_uninstall"
# after_app_uninstall = "construction_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "construction_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"construction_management.tasks.all"
# 	],
# 	"daily": [
# 		"construction_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"construction_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"construction_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"construction_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "construction_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "construction_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "construction_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["construction_management.utils.before_request"]
# after_request = ["construction_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["construction_management.utils.before_job"]
# after_job = ["construction_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"construction_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    # 1️⃣ الشركة
    {
        "dt": "Company",
        "filters": [["name", "in", ["COCO"]]]
    },

    # 2️⃣ وحدات القياس
    {
        "dt": "UOM",
        "filters": [["name", "in", [
            "قطعة", "يوم", "متر²", "متر³", "كغ", "متر", "لتر", "مجموعة", "وحدة", "متر مربع"
        ]]]
    },

    # 3️⃣ مجموعات الأصناف
    {
        "dt": "Item Group",
        "filters": [["name", "in", [
            "مواد صحية", "مواد بناء", "مواد كهربائية", "مواد تكييف",
            "مواد تشطيب", "أدوات", "خدمات", "معدات", "مواد خرسانة",
            "مواد تنسيق", "تراخيص"
        ]]]
    },

    # 4️⃣ الأصناف (Items)
    {
        "dt": "Item",
        "filters": [["item_code", "in", [
            "مراحيض", "أحواض ومغاسل", "صيانة وتركيب", "حجر وجص", "أسفلت", "وصلات وصمامات",
            "أدوات تركيب", "أدوات دهان", "دهانات", "مفصلات وأدوات", "خشب", "مواد لاصقة",
            "بلاط", "أسمنت وميكا", "وصلات وأدوات", "وحدات خارجية", "وحدات داخلية",
            "حساسات ودائرة", "أجهزة إنذار", "مصابيح", "مفاتيح وبرايز", "مفاتيح حماية",
            "لوحات فرعية", "لوحة توزيع رئيسية", "خراطيم إضافية", "أنابيب كوندوئيت",
            "موصلات أرضية", "أسلاك تأريض", "أنابيب صرف", "وصلات ومحابس",
            "أنابيب PVC", "مغاسل وأحواض", "أنابيب صرف صحي", "أنابيب مياه باردة/ساخنة",
            "رمل", "أسمنت", "بلوك إسمنتي", "قوالب خشب", "خرسانة مسلحة", "حديد تسليح",
            "خرسانة جاهزة", "مسامير وأدوات", "خشب نجارة", "نقل ناتج الحفر",
            "حفر آلي", "أدوات يدوية", "مواد تسوير مؤقت", "إيجار لوادر", "إيجار معدات تسوية",
            "خرسانة أساسية", "رمل وطين", "خشب شدادات", "بلوك طوب", "أسلاك كهربائية",
            "أنابيب مياه", "وصلات صرف صحي", "أحواض ومراحيض", "دهانات داخلية",
            "دهانات خارجية", "سيراميك وبلاط", "ألواح كلادينج", "نباتات وزهور",
            "تربة وسماد", "أدوات تنظيف", "مصعد كهربائي", "صيانة وتركيب مصعد",
            "أدوات فحص", "وحدات داخلية تكييف", "وحدة خارجية تكييف", "أنابيب تكييف",
            "عزل أنابيب تكييف", "أدوات كهرباء", "أدوات تكييف", "مواد حماية", "ترخيص بناء"
        ]]]
    },

    # 5️⃣ القوالب (Project Template)
    {
        "dt": "Project Template",
        "filters": [["name", "in", ["بناء عمارة"]]]
    },

    # 6️⃣ المشاريع
    {
        "dt": "Project",
        "filters": [["name", "in", ["PROJ-0006"]]]
    },

    # 7️⃣ المهام
    {
        "dt": "Task",
        "filters": [
            ["name", "in", [
                "TASK-2025-00057",
                "TASK-2025-00056",
                "TASK-2025-00055",
                "TASK-2025-00054",
                "TASK-2025-00061",
                "TASK-2025-00059",
                "TASK-2025-00060",
                "TASK-2025-00062",
                "TASK-2025-00069",
                "TASK-2025-00068",
                "TASK-2025-00067",
                "TASK-2025-00081",
                "TASK-2025-00066",
                "TASK-2025-00065",
                "TASK-2025-00064",
                "TASK-2025-00095",
                "TASK-2025-00094",
                "TASK-2025-00093",
                "TASK-2025-00092",
                "TASK-2025-00090",
                "TASK-2025-00089",
                "TASK-2025-00088",
                "TASK-2025-00085",
                "TASK-2025-00096",
                "TASK-2025-00091",
                "TASK-2025-00087",
                "TASK-2025-00086",
                "TASK-2025-00084",
                "TASK-2025-00083",
                "TASK-2025-00082",
                "TASK-2025-00080",
                "TASK-2025-00079",
                "TASK-2025-00078",
                "TASK-2025-00077",
                "TASK-2025-00076",
                "TASK-2025-00075",
                "TASK-2025-00074",
                "TASK-2025-00073",
                "TASK-2025-00072",
                "TASK-2025-00071",
                "TASK-2025-00070",
                "TASK-2025-00063",
                "TTMP-2025-00140",
                "TTMP-2025-00130",
                "TTMP-2025-00120",
                "TTMP-2025-00110",
                "TTMP-2025-00100",
                "TTMP-2025-00098",
                "TTMP-2025-00097",
                "TTMP-2025-00096",
                "TTMP-2025-00095",
                "TTMP-2025-00094",
                "TTMP-2025-00093",
                "TTMP-2025-00092",
                "TTMP-2025-00091",
                "TTMP-2025-00090",
                "TTMP-2025-00089",
                "TTMP-2025-00088",
                "TTMP-2025-00087",
                "TTMP-2025-00086",
                "TTMP-2025-00085",
                "TTMP-2025-00084",
                "TTMP-2025-00083",
                "TTMP-2025-00082",
                "TTMP-2025-00081",
                "TTMP-2025-00080",
                "TTMP-2025-00074",
                "TTMP-2025-00073",
                "TTMP-2025-00072",
                "TTMP-2025-00071",
                "TTMP-2025-00070",
                "TTMP-2025-00063",
                "TTMP-2025-00062",
                "TTMP-2025-00061",
                "TTMP-2025-00060",
                "TTMP-2025-00050",
                "TTMP-2025-00040",
                "TTMP-2025-00030",
                "TTMP-2025-00020",
                "TTMP-2025-00014",
                "TTMP-2025-00013",
                "TTMP-2025-00012",
                "TTMP-2025-00011",
                "TTMP-2025-00010",
            ]]
        ],
        "name": "task_childrens"
    },

    {
        "dt": "Task",
        "filters": [
            ["name", "in", [
                "TASK-2025-00045","TASK-2025-00046","TASK-2025-00047","TASK-2025-00048",
                "TASK-2025-00049","TASK-2025-00050","TASK-2025-00051","TASK-2025-00052",
                "TASK-2025-00053","TTMP-2025-00009",
                "TTMP-2025-00008",
                "TTMP-2025-00007",
                "TTMP-2025-00006",
                "TTMP-2025-00005",
                "TTMP-2025-00004",
                "TTMP-2025-00003",
                "TTMP-2025-00002",
                "TTMP-2025-00001",
            ]]
        ],
        "name": "task_parents"
    },







    # 8️⃣ أنواع الأنشطة
    {
        "dt": "Activity Type",
        "filters": [["name", "in", [
            "الإشراف الميداني", "تنسيق التراخيص", "أعمال حديد التسليح", "الهندسة الإنشائية",
            "نجارة القوالب", "أعمال البناء", "عمالة إنشائية", "الإشراف المعماري",
            "أعمال السباكة", "مساعد سباكة", "الهندسة الصحية", "تركيب الأنابيب",
            "أعمال الصرف الصحي", "أعمال التأريض الكهربائي", "مساعد كهرباء", "أعمال العزل المائي",
            "مساعد عزل مائي", "تركيب التركيبات", "مساعد تركيب", "أعمال الكهرباء",
            "تركيب المواسير", "سحب الكابلات", "تركيب لوحات التوزيع", "فني كهرباء",
            "تركيب المفاتيح", "أعمال التأريض", "أعمال إنذار الحريق", "أعمال التكييف",
            "مساعد تكييف", "تركيب أنابيب التكييف", "تركيب وحدات التكييف",
            "أعمال عزل التكييف", "تشغيل التكييف", "فني تكييف", "أعمال الدهان"
        ]]]
    },
    {
        "dt": "User",
        "filters": [["name", "in", [
            "pm@acc.com"
        ]]]
    },


    {
        "dt": "Department",
        "filters": [["name", "in", [
            "الموقع - C","الإدارة - C"
        ]]]
    },
    # 9️⃣ الموظفين
    {
        "dt": "Employee",
        "filters": [["name", "in", [
            "PR-EMP-00001","PR-EMP-00002","PR-EMP-00003","PR-EMP-00004","PR-EMP-00005",
            "PR-EMP-00006","PR-EMP-00007","PR-EMP-00008","PR-EMP-00009","PR-EMP-00010",
            "PR-EMP-00011","PR-EMP-00012","PR-EMP-00013","PR-EMP-00014","PR-EMP-00015",
            "PR-EMP-00016","PR-EMP-00017","PR-EMP-00018","PR-EMP-00019"
        ]]]
    },

    # 🔟 أنواع المطالبات
    {
        "dt": "Expense Claim Type",
        "filters": [["name", "in", [
            "رسوم إضافية","رسوم بلدية","مصروفات مراجعة","رسوم دفاع مدني","طباعة وثائق",
            "أدوات تصليح","أدوات فحص","منظفات ومعدات","فحص نهائي","أدوات تنظيف نهائي",
            "أدوات تشطيب خارجي","مواد تشطيب","أدوات","أدوات قياس","فحص وتشغيل",
            "أدوات تركيب","مواد عزل","موصلات","أسلاك تأريض","تصريح مبدئي","لوحات المشروع"
        ]]]
    },

    # 11️⃣ المطالبات (Expense Claims)
    {
        "dt": "Expense Claim",
        "filters": [["name", "in", [
            "EXP-2025-00001","EXP-2025-00002","EXP-2025-00003","EXP-2025-00004","EXP-2025-00005",
            "EXP-2025-00006","EXP-2025-00007","EXP-2025-00008","EXP-2025-00009","EXP-2025-00010",
            "EXP-2025-00011","EXP-2025-00012","EXP-2025-00013","EXP-2025-00014","EXP-2025-00015",
            "EXP-2025-00016","EXP-2025-00017","EXP-2025-00018","EXP-2025-00019"
        ]]]
    },

    # 12️⃣ الموردين
    {
        "dt": "Supplier",
        "filters": [["name", "in", ["ddd"]]]
    },

    # 13️⃣ طلبات المواد
    {
        "dt": "Material Request",
        "filters": [["name", "in", ["MATC-00001"]]]
    },

    # 14️⃣ فواتير الشراء
    {
        "dt": "Purchase Invoice",
        "filters": [["name", "in", [
            "ACC-PIP-2025-00001","ACC-PIP-2025-00002","ACC-PIP-2025-00003","ACC-PIP-2025-00004",
            "ACC-PIP-2025-00005","ACC-PIP-2025-00006","ACC-PIP-2025-00007","ACC-PIP-2025-00008",
            "ACC-PIP-2025-00009","ACC-PIP-2025-00010","ACC-PIP-2025-00011","ACC-PIP-2025-00012",
            "ACC-PIP-2025-00013","ACC-PIP-2025-00014","ACC-PIP-2025-00015","ACC-PIP-2025-00016",
            "ACC-PIP-2025-00017","ACC-PIP-2025-00018","ACC-PIP-2025-00019","ACC-PIP-2025-00020"
        ]]]
    },

    # 15️⃣ التايم شيت (Timesheets)
    {
        "dt": "Timesheet",
        "filters": [["name", "in", [
            "DTS-001","DTS-002","DTS-003","DTS-004","DTS-005","DTS-006","DTS-007",
            "DTS-008","DTS-009","DTS-010","DTS-011","DTS-012","DTS-013","DTS-014",
            "DTS-015","DTS-016","DTS-017","DTS-018","DTS-019","DTS-020"
        ]]]
    },

    # 16️⃣ التقارير (Reports)
    {
        "dt": "Report",
        "filters": [["name", "like", "Project_Calc%"]]
    },
    {
        "dt": "Purchase Invoice",
        "filters": [
            ["name", "in", [
                "ACC-PIP-2025-00001",
                "ACC-PIP-2025-00002",
                "ACC-PIP-2025-00003",
                "ACC-PIP-2025-00004",
                "ACC-PIP-2025-00005",
                "ACC-PIP-2025-00006",
                "ACC-PIP-2025-00007",
                "ACC-PIP-2025-00008",
                "ACC-PIP-2025-00009",
                "ACC-PIP-2025-00010",
                "ACC-PIP-2025-00011",
                "ACC-PIP-2025-00012",
                "ACC-PIP-2025-00013",
                "ACC-PIP-2025-00014",
                "ACC-PIP-2025-00015",
                "ACC-PIP-2025-00016",
                "ACC-PIP-2025-00017",
                "ACC-PIP-2025-00018",
                "ACC-PIP-2025-00019",
                "ACC-PIP-2025-00020",
                "ACC-PIP-2025-00021",
                "ACC-PIP-2025-00022",
                "ACC-PIP-2025-00023",
                "ACC-PIP-2025-00024",
                "ACC-PIP-2025-00025",
                "ACC-PIP-2025-00026",
                "ACC-PIP-2025-00027",
                "ACC-PIP-2025-00028",
                "ACC-PIP-2025-00029",
                "ACC-PIP-2025-00030",
                "ACC-PIP-2025-00031",
                "ACC-PIP-2025-00032",
                "ACC-PIP-2025-00033",
                "ACC-PIP-2025-00034",
                "ACC-PIP-2025-00035",
                "ACC-PIP-2025-00036",
                "ACC-PIP-2025-00037",
                "ACC-PIP-2025-00038",
                "ACC-PIP-2025-00039",
                "ACC-PIP-2025-00040",
                "ACC-PIP-2025-00041",
                "ACC-PIP-2025-00042",
                "ACC-PIP-2025-00043",
                "ACC-PIP-2025-00044",
                "ACC-PIP-2025-00045",
                "ACC-PIP-2025-00046",
                "ACC-PIP-2025-00047",
                "ACC-PIP-2025-00048",
                "ACC-PIP-2025-00049",
                "ACC-PIP-2025-00050",
                "ACC-PIP-2025-00051",
                "ACC-PIP-2025-00052",
                "ACC-PIP-2025-00053",
                "ACC-PIP-2025-00054",
                "ACC-PIP-2025-00055",
                "ACC-PIP-2025-00056",
                "ACC-PIP-2025-00057",
                "ACC-PIP-2025-00058",
                "ACC-PIP-2025-00059",
                "ACC-PIP-2025-00060",
                "ACC-PIP-2025-00061",
                "ACC-PIP-2025-00062",
                "ACC-PIP-2025-00063",
                "ACC-PIP-2025-00064",
                "ACC-PIP-2025-00065",
                "ACC-PIP-2025-00066",
                "ACC-PIP-2025-00067",
                "ACC-PIP-2025-00068",
                "ACC-PIP-2025-00069",
                "ACC-PIP-2025-00070",
                "ACC-PIP-2025-00071",
                "ACC-PIP-2025-00072",
                "ACC-PIP-2025-00073",
                "ACC-PIP-2025-00074",
                "ACC-PIP-2025-00075",
                "ACC-PIP-2025-00076",
                "ACC-PIP-2025-00077",
                "ACC-PIP-2025-00078",
                "ACC-PIP-2025-00079",
                "ACC-PIP-2025-00080",
                "ACC-PIP-2025-00081"
            ]]
        ]
    },
]
