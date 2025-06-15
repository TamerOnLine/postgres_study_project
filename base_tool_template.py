# 🧠 TEMPLATE: لإعادة الاستخدام في أي أداة داخل مجلد tools/

import os
import sys

# 🧭 إضافة المسار الجذر للمشروع
CURRENT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(CURRENT, "../../../"))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

def run_tool_template(tool_function, title="Tool Runner"):
    print(f"\n🔧 Running tool: {title}\n{'=' * (18 + len(title))}\n")
    try:
        tool_function()
    except Exception as e:
        print(f"❌ Error while running the tool: {e}")
    print(f"\n✅ Done: {title}\n{'=' * (18 + len(title))}\n")
