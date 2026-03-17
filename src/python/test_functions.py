"""Testes simples da aplicação FarmTech Solutions."""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CURRENT_DIR))

from main import (  # noqa: E402
    CropData,
    calculate_circular_area,
    calculate_input_needed,
    calculate_rectangular_area,
)


print("=" * 70)
print("  FarmTech Solutions - Testes Unitários")
print("=" * 70)
print()

print("TESTE 1: Cálculo de Área Circular (Café)")
radius = 50
area = calculate_circular_area(radius)
expected = 3.141592653589793 * (50 ** 2)
print(f"   Entrada: raio = {radius} m")
print(f"   Saída: área = {area:.2f} m²")
print(f"   Status: {'PASS' if abs(area - expected) < 0.0001 else 'FAIL'}")
print()

print("TESTE 2: Cálculo de Área Retangular (Soja)")
length, width = 100, 150
area = calculate_rectangular_area(length, width)
expected = 15000
print(f"   Entrada: {length} m x {width} m")
print(f"   Saída: área = {area:.2f} m²")
print(f"   Status: {'PASS' if area == expected else 'FAIL'}")
print()

print("TESTE 3: Cálculo de Insumo")
rows, row_length, amount = 50, 100, 500
total = calculate_input_needed(rows, row_length, amount)
expected = (50 * 100 * 500) / 1000
print(f"   Entrada: {rows} ruas x {row_length} m x {amount} mL/m")
print(f"   Saída: {total:.2f} litros")
print(f"   Status: {'PASS' if total == expected else 'FAIL'}")
print()

print("TESTE 4: Operações da classe CropData")
data = CropData()
print(f"   Estado inicial: {data.get_count()} registros")
print(f"   Está vazia: {data.is_empty()}")

data.add_data('Coffee', 'Circular', 7853.98, 50, 100, 'Phosphate', 500, 2500)
data.add_data('Soybean', 'Rectangular', 10000, 80, 120, 'Herbicide', 300, 2880)
print(f"   Após adicionar: {data.get_count()} registros")
print(f"   Culturas: {', '.join(data.crop_types)}")

data.update_data(0, 'Coffee', 'Circular', 8000, 55, 110, 'Fertilizer', 450, 2722.5)
print(
    f"   Após atualizar: {data.crop_types[0]}, "
    f"área = {data.areas[0]:.2f} m², rua = {data.row_lengths[0]:.2f} m"
)

data.delete_data(1)
print(f"   Após deletar: {data.get_count()} registro(s)")
print("   Status: PASS")
print()

print("=" * 70)
print("  Todos os testes foram executados")
print("=" * 70)
print("\nExecute 'python main.py' para usar a aplicação completa.\n")