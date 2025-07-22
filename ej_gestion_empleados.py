class Empleado:
    def __init__(self, nombre, dni, salario_base):
        self.nombre = nombre
        self.dni = dni
        self.salario_base = salario_base

    def calcular_salario_anual(self):
        return self.salario_base * 12

    def mostrar_info(self):
        return f"{self.nombre} (DNI: {self.dni}) - Salario mensual: {self.salario_base}€"


class Gerente(Empleado):
    def __init__(self, nombre, dni, salario_base, bono):
        super().__init__(nombre, dni, salario_base)
        self.bono = bono

    def calcular_salario_anual(self):
        return super().calcular_salario_anual() + self.bono

    def mostrar_info(self):
        return super().mostrar_info() + f" [GERENTE, Bono anual: {self.bono}€]"


class Tecnico(Empleado):
    def __init__(self, nombre, dni, salario_base, horas_extra, precio_hora):
        super().__init__(nombre, dni, salario_base)
        self.horas_extra = horas_extra
        self.precio_hora = precio_hora

    def calcular_salario_anual(self):
        extra = self.horas_extra * self.precio_hora * 12
        return super().calcular_salario_anual() + extra

    def mostrar_info(self):
        return super().mostrar_info() + f" [TÉCNICO, {self.horas_extra}h extra/mes a {self.precio_hora}€/h]"


class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        print("\n📋 Lista de empleados:")
        for emp in self.empleados:
            print("-", emp.mostrar_info())

    def buscar_empleado_por_dni(self, dni):
        for emp in self.empleados:
            if emp.dni == dni:
                return emp
        return None


# -------------------------------
# 🚀 PROGRAMA PRINCIPAL
# -------------------------------
def menu():
    print("\n--- MENÚ DE GESTIÓN DE EMPLEADOS ---")
    print("1. Agregar Empleado Base")
    print("2. Agregar Gerente")
    print("3. Agregar Técnico")
    print("4. Listar empleados")
    print("5. Buscar empleado por DNI")
    print("6. Salir")

empresa = Empresa()

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        salario = float(input("Salario base: "))
        emp = Empleado(nombre, dni, salario)
        empresa.agregar_empleado(emp)
        print("✅ Empleado agregado.")

    elif opcion == "2":
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        salario = float(input("Salario base: "))
        bono = float(input("Bono anual: "))
        gerente = Gerente(nombre, dni, salario, bono)
        empresa.agregar_empleado(gerente)
        print("✅ Gerente agregado.")

    elif opcion == "3":
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        salario = float(input("Salario base: "))
        horas = float(input("Horas extra mensuales: "))
        precio = float(input("Precio por hora extra: "))
        tecnico = Tecnico(nombre, dni, salario, horas, precio)
        empresa.agregar_empleado(tecnico)
        print("✅ Técnico agregado.")

    elif opcion == "4":
        empresa.listar_empleados()

    elif opcion == "5":
        dni = input("Introduce el DNI del empleado: ")
        empleado = empresa.buscar_empleado_por_dni(dni)
        if empleado:
            print("🔎 Empleado encontrado:")
            print(empleado.mostrar_info())
            print("Salario anual:", empleado.calcular_salario_anual(), "€")
        else:
            print("❌ No se encontró ningún empleado con ese DNI.")

    elif opcion == "6":
        print("👋 Saliendo del programa...")
        break

    else:
        print("❌ Opción no válida.")