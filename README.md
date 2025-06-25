# 📦 Backend da Aplicação

Este é o repositório do **backend** da aplicação. A aplicação foi desenvolvida em **Python** e deve ser executada na **porta 8004**.

## 🚀 Como rodar o backend

Siga os passos abaixo para executar a aplicação localmente:

---

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

---

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

---

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Rode as migrações (se for um projeto Django)

```bash
python manage.py migrate
```

---

### 5️⃣ Inicie o servidor na porta 8004

```bash
python manage.py runserver 0.0.0.0:8004
```

---

## 🌐 Acesso

Se estiver rodando localmente, acesse:

```
http://127.0.0.1:8004/
```

---

## 💡 Observação

👉 A aplicação foi projetada para rodar especificamente na porta **8004**.  
👉 Certifique-se de que essa porta está disponível no seu ambiente antes de iniciar o servidor.
