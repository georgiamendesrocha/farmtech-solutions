"""
FarmTech Solutions - Digital Agriculture Management System
Main application for managing crop cultivation data

Supports: Coffee and Soybean crops
Features: Area calculation, input management, data operations
"""

import math
import os
import sys


class CropData:
    """Class to store crop cultivation data"""
    
    def __init__(self):
        self.crop_types = []        # Type of crop (Coffee or Soybean)
        self.areas = []             # Planting area in square meters
        self.rows = []              # Number of rows in the field
        self.input_products = []    # Input product used (fertilizer, pesticide, etc.)
        self.input_amounts = []     # Amount of input per meter (mL/m)
    
    def add_data(self, crop_type, area, rows, product, amount):
        """Add new crop data to vectors"""
        self.crop_types.append(crop_type)
        self.areas.append(area)
        self.rows.append(rows)
        self.input_products.append(product)
        self.input_amounts.append(amount)
    
    def update_data(self, index, crop_type, area, rows, product, amount):
        """Update existing data at specific index"""
        if 0 <= index < len(self.crop_types):
            self.crop_types[index] = crop_type
            self.areas[index] = area
            self.rows[index] = rows
            self.input_products[index] = product
            self.input_amounts[index] = amount
            return True
        return False
    
    def delete_data(self, index):
        """Delete data at specific index"""
        if 0 <= index < len(self.crop_types):
            self.crop_types.pop(index)
            self.areas.pop(index)
            self.rows.pop(index)
            self.input_products.pop(index)
            self.input_amounts.pop(index)
            return True
        return False
    
    def get_count(self):
        """Return number of records"""
        return len(self.crop_types)
    
    def is_empty(self):
        """Check if data is empty"""
        return len(self.crop_types) == 0


def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')


def pause():
    """Pause execution and wait for user input"""
    input("\nPressione ENTER para continuar...")


def calculate_rectangular_area(length, width):
    """Calculate rectangular area (for Soybean fields)"""
    return length * width


def calculate_circular_area(radius):
    """Calculate circular area (for Coffee plantations)"""
    return math.pi * (radius ** 2)


def calculate_input_needed(rows, row_length, amount_per_meter):
    """
    Calculate total input needed for crop management
    
    Parameters:
    - rows: number of rows in the field
    - row_length: length of each row in meters
    - amount_per_meter: amount of input per meter (in mL)
    
    Returns: total amount in liters
    """
    total_meters = rows * row_length
    total_ml = total_meters * amount_per_meter
    total_liters = total_ml / 1000  # Convert mL to L
    return total_liters


def display_header(title):
    """Display formatted header"""
    clear_screen()
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)
    print()


def display_main_menu():
    """Display main menu options"""
    display_header("FarmTech Solutions - Menu Principal")
    print("1. Entrada de Dados (Adicionar nova cultura)")
    print("2. Saída de Dados (Visualizar todas as culturas)")
    print("3. Atualizar Dados (Modificar registro existente)")
    print("4. Deletar Dados (Remover registro)")
    print("5. Sair do Programa")
    print()


def input_data(crop_data):
    """Handle data input for new crop"""
    display_header("Entrada de Dados - Nova Cultura")
    
    # Select crop type
    print("Escolha o tipo de cultura:")
    print("1. Café (Coffee)")
    print("2. Soja (Soybean)")
    print()
    
    while True:
        try:
            crop_choice = int(input("Digite sua escolha (1 ou 2): "))
            if crop_choice in [1, 2]:
                break
            print("Opção inválida! Digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    if crop_choice == 1:
        crop_type = "Coffee"
        print("\n--- Cálculo de Área (Circular) ---")
        while True:
            try:
                radius = float(input("Digite o raio da área de plantio (em metros): "))
                if radius > 0:
                    break
                print("O raio deve ser maior que zero!")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        
        area = calculate_circular_area(radius)
        print(f"\nÁrea calculada: {area:.2f} m²")
        
    else:  # Soybean
        crop_type = "Soybean"
        print("\n--- Cálculo de Área (Retangular) ---")
        while True:
            try:
                length = float(input("Digite o comprimento da área (em metros): "))
                width = float(input("Digite a largura da área (em metros): "))
                if length > 0 and width > 0:
                    break
                print("Comprimento e largura devem ser maiores que zero!")
            except ValueError:
                print("Entrada inválida! Digite números.")
        
        area = calculate_rectangular_area(length, width)
        print(f"\nÁrea calculada: {area:.2f} m²")
    
    # Input management data
    print("\n--- Manejo de Insumos ---")
    product = input("Digite o nome do produto/insumo (ex: Fosfato, Herbicida): ")
    
    while True:
        try:
            rows = int(input("Digite o número de ruas/fileiras na lavoura: "))
            if rows > 0:
                break
            print("O número de ruas deve ser maior que zero!")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    while True:
        try:
            row_length = float(input("Digite o comprimento de cada rua (em metros): "))
            if row_length > 0:
                break
            print("O comprimento deve ser maior que zero!")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    while True:
        try:
            amount_per_meter = float(input("Digite a quantidade de insumo por metro (em mL/m): "))
            if amount_per_meter > 0:
                break
            print("A quantidade deve ser maior que zero!")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    # Calculate total input needed
    total_liters = calculate_input_needed(rows, row_length, amount_per_meter)
    
    print(f"\n--- Resultado do Cálculo ---")
    print(f"Total de metros lineares: {rows * row_length:.2f} m")
    print(f"Total de insumo necessário: {total_liters:.2f} litros")
    
    # Save data
    crop_data.add_data(crop_type, area, rows, product, amount_per_meter)
    
    print("\n✓ Dados salvos com sucesso!")
    pause()


def output_data(crop_data):
    """Display all stored crop data"""
    display_header("Saída de Dados - Todas as Culturas")
    
    if crop_data.is_empty():
        print("Nenhum dado cadastrado ainda.")
        pause()
        return
    
    for i in range(crop_data.get_count()):
        print(f"\n{'─' * 60}")
        print(f"Registro #{i + 1}")
        print(f"{'─' * 60}")
        print(f"Tipo de Cultura: {crop_data.crop_types[i]}")
        print(f"Área de Plantio: {crop_data.areas[i]:.2f} m²")
        print(f"Número de Ruas: {crop_data.rows[i]}")
        print(f"Produto/Insumo: {crop_data.input_products[i]}")
        print(f"Quantidade por Metro: {crop_data.input_amounts[i]:.2f} mL/m")
        
        # Estimate total input needed (assuming 100m rows as example)
        example_row_length = 100
        total_liters = calculate_input_needed(
            crop_data.rows[i], 
            example_row_length, 
            crop_data.input_amounts[i]
        )
        print(f"Insumo Estimado (ruas de {example_row_length}m): {total_liters:.2f} litros")
    
    print(f"\n{'─' * 60}")
    print(f"Total de registros: {crop_data.get_count()}")
    pause()


def update_data(crop_data):
    """Update existing crop data"""
    display_header("Atualizar Dados - Modificar Registro")
    
    if crop_data.is_empty():
        print("Nenhum dado cadastrado para atualizar.")
        pause()
        return
    
    # Show current data
    print("Registros disponíveis:\n")
    for i in range(crop_data.get_count()):
        print(f"{i + 1}. {crop_data.crop_types[i]} - Área: {crop_data.areas[i]:.2f} m²")
    
    print()
    while True:
        try:
            choice = int(input(f"Digite o número do registro para atualizar (1-{crop_data.get_count()}): "))
            if 1 <= choice <= crop_data.get_count():
                break
            print(f"Opção inválida! Digite um número entre 1 e {crop_data.get_count()}.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    index = choice - 1
    
    print(f"\nAtualizando registro #{choice}...")
    print("Digite os novos dados:\n")
    
    # Similar input process as input_data
    print("Escolha o tipo de cultura:")
    print("1. Café (Coffee)")
    print("2. Soja (Soybean)")
    
    while True:
        try:
            crop_choice = int(input("Digite sua escolha (1 ou 2): "))
            if crop_choice in [1, 2]:
                break
            print("Opção inválida! Digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    if crop_choice == 1:
        crop_type = "Coffee"
        while True:
            try:
                radius = float(input("Digite o raio da área (em metros): "))
                if radius > 0:
                    break
                print("O raio deve ser maior que zero!")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        area = calculate_circular_area(radius)
    else:
        crop_type = "Soybean"
        while True:
            try:
                length = float(input("Digite o comprimento da área (em metros): "))
                width = float(input("Digite a largura da área (em metros): "))
                if length > 0 and width > 0:
                    break
                print("Comprimento e largura devem ser maiores que zero!")
            except ValueError:
                print("Entrada inválida! Digite números.")
        area = calculate_rectangular_area(length, width)
    
    product = input("Digite o nome do produto/insumo: ")
    
    while True:
        try:
            rows = int(input("Digite o número de ruas: "))
            if rows > 0:
                break
            print("O número de ruas deve ser maior que zero!")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    while True:
        try:
            amount = float(input("Digite a quantidade por metro (mL/m): "))
            if amount > 0:
                break
            print("A quantidade deve ser maior que zero!")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    # Update data
    crop_data.update_data(index, crop_type, area, rows, product, amount)
    
    print("\n✓ Dados atualizados com sucesso!")
    pause()


def delete_data(crop_data):
    """Delete crop data"""
    display_header("Deletar Dados - Remover Registro")
    
    if crop_data.is_empty():
        print("Nenhum dado cadastrado para deletar.")
        pause()
        return
    
    # Show current data
    print("Registros disponíveis:\n")
    for i in range(crop_data.get_count()):
        print(f"{i + 1}. {crop_data.crop_types[i]} - Área: {crop_data.areas[i]:.2f} m²")
    
    print()
    while True:
        try:
            choice = int(input(f"Digite o número do registro para deletar (1-{crop_data.get_count()}): "))
            if 1 <= choice <= crop_data.get_count():
                break
            print(f"Opção inválida! Digite um número entre 1 e {crop_data.get_count()}.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    index = choice - 1
    
    # Confirm deletion
    print(f"\nVocê tem certeza que deseja deletar o registro #{choice}?")
    print(f"Cultura: {crop_data.crop_types[index]}")
    confirm = input("Digite 'SIM' para confirmar: ")
    
    if confirm.upper() == 'SIM':
        crop_data.delete_data(index)
        print("\n✓ Registro deletado com sucesso!")
    else:
        print("\nOperação cancelada.")
    
    pause()


def export_data_to_csv(crop_data):
    """Export data to CSV file for R analysis"""
    if crop_data.is_empty():
        return
    
    data_dir = "../../data"
    os.makedirs(data_dir, exist_ok=True)
    
    csv_path = os.path.join(data_dir, "crop_data.csv")
    
    try:
        with open(csv_path, 'w') as f:
            # Write header
            f.write("crop_type,area_m2,rows,input_product,input_amount_ml_per_m\n")
            
            # Write data
            for i in range(crop_data.get_count()):
                f.write(f"{crop_data.crop_types[i]},")
                f.write(f"{crop_data.areas[i]:.2f},")
                f.write(f"{crop_data.rows[i]},")
                f.write(f"{crop_data.input_products[i]},")
                f.write(f"{crop_data.input_amounts[i]:.2f}\n")
        
        print(f"\n✓ Dados exportados para: {csv_path}")
    except Exception as e:
        print(f"\n✗ Erro ao exportar dados: {e}")


def main():
    """Main program loop"""
    crop_data = CropData()
    
    while True:
        display_main_menu()
        
        try:
            choice = input("Digite sua escolha (1-5): ")
            
            if choice == '1':
                input_data(crop_data)
            elif choice == '2':
                output_data(crop_data)
            elif choice == '3':
                update_data(crop_data)
            elif choice == '4':
                delete_data(crop_data)
            elif choice == '5':
                display_header("Encerrando Programa")
                
                # Export data before exiting
                if not crop_data.is_empty():
                    export_data_to_csv(crop_data)
                
                print("Obrigado por usar o FarmTech Solutions!")
                print("Até logo! 🌱")
                sys.exit(0)
            else:
                print("\nOpção inválida! Por favor, escolha uma opção de 1 a 5.")
                pause()
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            sys.exit(0)
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            pause()


if __name__ == "__main__":
    main()
