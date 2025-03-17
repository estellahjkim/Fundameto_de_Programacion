class CuentaBancaria:
    __contador_cuentas = 0
    __cuentas[str, list] = {}

    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0
        self.__class__.__contador_cuentas += 1
        nuemro_cuenta = self.__class__.__contador_cuentas
        self.__codigo_cuenta = f"CB-{nuemro_cuenta:03d}"
        if titular in CuentaBancaria.__cuentas:
            CuentaBancaria.__cuentas[titular].append(self)
        else:
            CuentaBancaria.__cuentas[titular] = [self]

    @property
    def titular(self):
        return self.__titular

    @property
    def codigo_cuenta(self):
        return self.__codigo_cuenta

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, cuantia):
        if cuantia < 0:
            raise ValueError()
        self.__sado += cuantia

    def retirar(self, cuantia):
        if self.__saldo < cuantia or cuantia < 0:
            raise ValueError()
        self.__sado -= cuantia

    @classmethod
    def obtener_total_cuentas(cls):
        return cls.__contador_cuentas

    @classmethod
    def total_saldo_titular(cls, titular):
        cuentas = cls.__cuentas.get(titular, [])
        suma_saldos = 0
        for cuenta in cuentas:
            suma_saldo += cuenta.saldo
        return suma_saldo

    def __str__(self):
        cc = self.codigo_cuenta
        tit = self.titular
        sal = self.saldo
        return f"{cc} - Titular: {tit}, Saldo: {sal}"
