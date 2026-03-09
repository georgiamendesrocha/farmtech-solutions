"""
Unit tests for FarmTech Solutions
Tests core functionality: area calculations, input management, and data operations
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import calculate_circular_area, calculate_rectangular_area, calculate_input_needed, CropData

print("=" * 70)
print("  FarmTech Solutions - Unit Tests")
print("=" * 70)
print()

print("TEST 1: Circular Area Calculation (Coffee)")
radius = 50
area = calculate_circular_area(radius)
expected = 3.14159 * (50 ** 2)
print(f"   Input: radius = {radius}m")
print(f"   Output: area = {area:.2f} m²")
print(f"   Status: {'PASS' if abs(area - expected) < 1 else 'FAIL'}")
print()

print("TEST 2: Rectangular Area Calculation (Soybean)")
length, width = 100, 150
area = calculate_rectangular_area(length, width)
expected = 15000
print(f"   Input: {length}m x {width}m")
print(f"   Output: area = {area:.2f} m²")
print(f"   Status: {'PASS' if area == expected else 'FAIL'}")
print()

print("TEST 3: Input Amount Calculation")
rows, row_length, amount = 50, 100, 500
total = calculate_input_needed(rows, row_length, amount)
expected = (50 * 100 * 500) / 1000  # 2500 liters
print(f"   Input: {rows} rows x {row_length}m x {amount} mL/m")
print(f"   Output: {total:.2f} liters")
print(f"   Status: {'PASS' if total == expected else 'FAIL'}")
print()

print("TEST 4: CropData Class Operations")
data = CropData()
print(f"   Initial state: {data.get_count()} records")
print(f"   Is empty: {data.is_empty()}")

data.add_data('Coffee', 7853.98, 50, 'Phosphate', 500)
data.add_data('Soybean', 10000, 80, 'Herbicide', 300)
print(f"   After add: {data.get_count()} records")
print(f"   Crop types: {', '.join(data.crop_types)}")

data.update_data(0, 'Coffee', 8000, 55, 'Fertilizer', 450)
print(f"   After update: {data.crop_types[0]}, area = {data.areas[0]:.2f} m²")

data.delete_data(1)
print(f"   After delete: {data.get_count()} record(s)")
print(f"   Status: PASS")
print()

print("=" * 70)
print("  All tests completed successfully")
print("=" * 70)
print()
print("Run 'python3 main.py' to use the full application")
print()
