"""
FarmTech Solutions - Sistema de Agricultura Digital
Aplicação principal em Python para cadastro de culturas, cálculo de área
plantada e manejo de insumos.

Culturas suportadas:
- Café (área circular)
- Soja (área retangular)
"""

from __future__ import annotations

import csv
import math
import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
CSV_FILE = DATA_DIR / "crop_data.csv"


class CropData:
    """Armazena os dados da aplicação em vetores/listas paralelas."""

    def __init__(self) -> None:
        self.crop_types = []
        self.area_shapes = []
        self.areas = []
        self.rows = []
        self.row_lengths = []
        self.input_products = []
        self.input_amounts = []
        self.total_input_liters = []

    def add_data(
        self,
        crop_type: str,
        area_shape: str,
        area: float,
        rows: int,
        row_length: float,
        product: str,
        amount_per_meter: float,
        total_liters: float,
    ) -> None:
        self.crop_types.append(crop_type)
        self.area_shapes.append(area_shape)
        self.areas.append(area)
        self.rows.append(rows)
        self.row_lengths.append(row_length)
        self.input_products.append(product)
        self.input_amounts.append(amount_per_meter)
        self.total_input_liters.append(total_liters)

    def update_data(
        self,
        index: int,
        crop_type: str,
        area_shape: str,
        area: float,
        rows: int,
        row_length: float,
        product: str,
        amount_per_meter: float,
        total_liters: float,
    ) -> bool:
        if 0 <= index < len(self.crop_types):
            self.crop_types[index] = crop_type
            self.area_shapes[index] = area_shape
            self.areas[index] = area
            self.rows[index] = rows
            self.row_lengths[index] = row_length
            self.input_products[index] = product
            self.input_amounts[index] = amount_per_meter
            self.total_input_liters[index] = total_liters
            return True
        return False

    def delete_data(self, index: int) -> bool:
        if 0 <= index < len(self.crop_types):
            self.crop_types.pop(index)
            self.area_shapes.pop(index)
            self.areas.pop(index)
            self.rows.pop(index)
            self.row_lengths.pop(index)
            self.input_products.pop(index)
            self.input_amounts.pop(index)
            self.total_input_liters.pop(index)
            return True
        return False

    def get_count(self) -> int:
        return len(self.crop_types)

    def is_empty(self) -> bool:
        return self.get_count() == 0


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    input("\nPressione ENTER para continuar...")


def calculate_rectangular_area(length: float, width: float) -> float:
    return length * width


def calculate_circular_area(radius: float) -> float:
    return math.pi * (radius ** 2)


def calculate_input_needed(rows: int, row_length: float, amount_per_meter: float) -> float:
    total_meters = rows * row_length
    total_ml = total_meters * amount_per_meter
    return total_ml / 1000.0


def display_header(title: str) -> None:
    clear_screen()
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)
    print()


def display_main_menu() -> None:
    display_header("FarmTech Solutions - Menu Principal")
    print("1. Entrada de Dados (Adicionar nova cultura)")
    print("2. Saída de Dados (Visualizar todas as culturas)")
    print("3. Atualizar Dados (Modificar registro existente)")
    print("4. Deletar Dados (Remover registro)")
    print("5. Sair do Programa")
    print()


def ask_int(prompt: str, min_value: int = 1) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            print(f"Valor inválido! Digite um número inteiro maior ou igual a {min_value}.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def ask_float(prompt: str, min_value: float = 0.0) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value > min_value:
                return value
            print(f"Valor inválido! Digite um número maior que {min_value}.")
        except ValueError:
            print("Entrada inválida! Digite um número.")


def choose_crop_type() -> tuple[str, str, float]:
    print("Escolha o tipo de cultura:")
    print("1. Café (Coffee)")
    print("2. Soja (Soybean)")
    print()

    while True:
        choice = input("Digite sua escolha (1 ou 2): ").strip()
        if choice in {"1", "2"}:
            break
        print("Opção inválida! Digite 1 ou 2.")

    if choice == "1":
        crop_type = "Coffee"
        area_shape = "Circular"
        print("\n--- Cálculo de Área do Café (Figura Circular) ---")
        radius = ask_float("Digite o raio da área de plantio (em metros): ")
        area = calculate_circular_area(radius)
    else:
        crop_type = "Soybean"
        area_shape = "Rectangular"
        print("\n--- Cálculo de Área da Soja (Figura Retangular) ---")
        length = ask_float("Digite o comprimento da área (em metros): ")
        width = ask_float("Digite a largura da área (em metros): ")
        area = calculate_rectangular_area(length, width)

    print(f"\nÁrea calculada: {area:.2f} m²")
    return crop_type, area_shape, area


def collect_management_data() -> tuple[str, int, float, float, float]:
    print("\n--- Manejo de Insumos ---")
    product = input("Digite o nome do produto/insumo (ex: Fosfato, Herbicida): ").strip()
    while not product:
        print("O nome do produto não pode ficar vazio.")
        product = input("Digite o nome do produto/insumo: ").strip()

    rows = ask_int("Digite o número de ruas/fileiras na lavoura: ")
    row_length = ask_float("Digite o comprimento de cada rua (em metros): ")
    amount_per_meter = ask_float("Digite a quantidade de insumo por metro (em mL/m): ")

    total_liters = calculate_input_needed(rows, row_length, amount_per_meter)

    print("\n--- Resultado do Cálculo de Manejo ---")
    print(f"Total de metros lineares: {rows * row_length:.2f} m")
    print(f"Total de insumo necessário: {total_liters:.2f} litros")

    return product, rows, row_length, amount_per_meter, total_liters


def input_data(crop_data: CropData) -> None:
    display_header("Entrada de Dados - Nova Cultura")
    crop_type, area_shape, area = choose_crop_type()
    product, rows, row_length, amount_per_meter, total_liters = collect_management_data()

    crop_data.add_data(
        crop_type=crop_type,
        area_shape=area_shape,
        area=area,
        rows=rows,
        row_length=row_length,
        product=product,
        amount_per_meter=amount_per_meter,
        total_liters=total_liters,
    )

    print("\n✓ Dados salvos com sucesso!")
    pause()


def output_data(crop_data: CropData) -> None:
    display_header("Saída de Dados - Todas as Culturas")

    if crop_data.is_empty():
        print("Nenhum dado cadastrado ainda.")
        pause()
        return

    for i in range(crop_data.get_count()):
        print("─" * 70)
        print(f"Registro #{i + 1}")
        print("─" * 70)
        print(f"Tipo de Cultura:           {crop_data.crop_types[i]}")
        print(f"Figura Geométrica:         {crop_data.area_shapes[i]}")
        print(f"Área de Plantio:           {crop_data.areas[i]:.2f} m²")
        print(f"Número de Ruas:            {crop_data.rows[i]}")
        print(f"Comprimento de Cada Rua:   {crop_data.row_lengths[i]:.2f} m")
        print(f"Produto/Insumo:            {crop_data.input_products[i]}")
        print(f"Quantidade por Metro:      {crop_data.input_amounts[i]:.2f} mL/m")
        print(f"Total de Insumo:           {crop_data.total_input_liters[i]:.2f} litros")
        print()

    print("─" * 70)
    print(f"Total de registros: {crop_data.get_count()}")
    pause()


def choose_record_index(crop_data: CropData, action_label: str) -> int:
    print("Registros disponíveis:\n")
    for i in range(crop_data.get_count()):
        print(
            f"{i + 1}. {crop_data.crop_types[i]} | "
            f"Área: {crop_data.areas[i]:.2f} m² | "
            f"Produto: {crop_data.input_products[i]}"
        )
    print()

    while True:
        try:
            choice = int(input(f"Digite o número do registro para {action_label} (1-{crop_data.get_count()}): "))
            if 1 <= choice <= crop_data.get_count():
                return choice - 1
            print(f"Opção inválida! Digite um número entre 1 e {crop_data.get_count()}.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def update_data(crop_data: CropData) -> None:
    display_header("Atualizar Dados - Modificar Registro")

    if crop_data.is_empty():
        print("Nenhum dado cadastrado para atualizar.")
        pause()
        return

    index = choose_record_index(crop_data, "atualizar")
    print(f"\nAtualizando registro #{index + 1}...\n")

    crop_type, area_shape, area = choose_crop_type()
    product, rows, row_length, amount_per_meter, total_liters = collect_management_data()

    crop_data.update_data(
        index=index,
        crop_type=crop_type,
        area_shape=area_shape,
        area=area,
        rows=rows,
        row_length=row_length,
        product=product,
        amount_per_meter=amount_per_meter,
        total_liters=total_liters,
    )

    print("\n✓ Dados atualizados com sucesso!")
    pause()


def delete_data(crop_data: CropData) -> None:
    display_header("Deletar Dados - Remover Registro")

    if crop_data.is_empty():
        print("Nenhum dado cadastrado para deletar.")
        pause()
        return

    index = choose_record_index(crop_data, "deletar")

    print("\nVocê tem certeza que deseja deletar este registro?")
    print(f"Cultura: {crop_data.crop_types[index]}")
    print(f"Produto: {crop_data.input_products[index]}")
    confirm = input("Digite 'SIM' para confirmar: ").strip().upper()

    if confirm == "SIM":
        crop_data.delete_data(index)
        print("\n✓ Registro deletado com sucesso!")
    else:
        print("\nOperação cancelada.")

    pause()


def export_data_to_csv(crop_data: CropData) -> None:
    if crop_data.is_empty():
        print("\nNenhum dado para exportar.")
        return

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "crop_type",
                    "area_shape",
                    "area_m2",
                    "rows",
                    "row_length_m",
                    "input_product",
                    "input_amount_ml_per_m",
                    "total_input_liters",
                ]
            )

            for i in range(crop_data.get_count()):
                writer.writerow(
                    [
                        crop_data.crop_types[i],
                        crop_data.area_shapes[i],
                        f"{crop_data.areas[i]:.2f}",
                        crop_data.rows[i],
                        f"{crop_data.row_lengths[i]:.2f}",
                        crop_data.input_products[i],
                        f"{crop_data.input_amounts[i]:.2f}",
                        f"{crop_data.total_input_liters[i]:.2f}",
                    ]
                )

        print(f"\n✓ Dados exportados com sucesso para: {CSV_FILE}")
    except OSError as exc:
        print(f"\n✗ Erro ao exportar dados: {exc}")


def main() -> None:
    crop_data = CropData()

    while True:
        display_main_menu()
        choice = input("Digite sua escolha (1-5): ").strip()

        try:
            if choice == "1":
                input_data(crop_data)
            elif choice == "2":
                output_data(crop_data)
            elif choice == "3":
                update_data(crop_data)
            elif choice == "4":
                delete_data(crop_data)
            elif choice == "5":
                display_header("Encerrando Programa")
                if not crop_data.is_empty():
                    export_data_to_csv(crop_data)
                print("Obrigado por usar o FarmTech Solutions!")
                print("Até logo! 🌱")
                break
            else:
                print("\nOpção inválida! Escolha uma opção de 1 a 5.")
                pause()
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as exc:
            print(f"\nErro inesperado: {exc}")
            pause()


if __name__ == "__main__":
    main()