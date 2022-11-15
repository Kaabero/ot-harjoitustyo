
```mermaid
sequenceDiagram
  participant main
  main->>kone: Machine()
  kone->>tankki: FuelTank()
  kone->>tankki: fill(40)
  tankki->>moottori: Engine(tankki)
  main->>kone: drive()
  kone->>moottori: start()
  moottori->>tankki: consume(5)
  kone->>moottori: is_running()
  moottori->>tankki: fuel_contents()
  tankki-->>moottori: 35
  moottori-->>kone: 35 > 0
  kone->>moottori: use_energy()
  moottori->>tankki: consume(10)
 

```
 
