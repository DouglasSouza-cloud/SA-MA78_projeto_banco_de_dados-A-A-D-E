 -- 1. Tabela: CARGO
CREATE TABLE cargo (
   id_cargo BIGINT AUTO_INCREMENT PRIMARY KEY,
   nome_cargo VARCHAR(100) NOT NULL,
   descricao_cargo TEXT,
   nivel_hierarquico_cargo INT NOT NULL DEFAULT 1,
   salario_base_cargo DECIMAL(15,2),
   status_cargo VARCHAR(20) DEFAULT 'Ativo',
   CONSTRAINT chk_status_cargo CHECK (status_cargo IN ('Ativo', 'Inativo'))
);
 
-- 2. Tabela: COLABORADOR
CREATE TABLE colaborador (
   id_colaborador BIGINT AUTO_INCREMENT PRIMARY KEY,
   nome_colaborador VARCHAR(255) NOT NULL,
   cpf_colaborador VARCHAR(11) NOT NULL UNIQUE,
   data_nascimento_colaborador DATE,
   email_colaborador VARCHAR(100) NOT NULL UNIQUE,
   telefone_colaborador VARCHAR(20),
   data_admissao_colaborador DATE NOT NULL,
   data_demissao_colaborador DATE,
   status_colaborador VARCHAR(20) DEFAULT 'Ativo',
   id_cargo_colaborador BIGINT NOT NULL,
   FOREIGN KEY (id_cargo_colaborador) REFERENCES cargo(id_cargo),
   CONSTRAINT chk_status_colaborador CHECK (status_colaborador IN ('Ativo', 'Inativo', 'Afastado', 'Demitido'))
);
CREATE INDEX idx_colaborador_cargo ON colaborador(id_cargo_colaborador);
 
-- 3. Tabela: USUARIO (acesso ao sistema, 1:1 com colaborador)
CREATE TABLE usuario (
   id_usuario BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_colaborador_usuario BIGINT NOT NULL UNIQUE,
   login_usuario VARCHAR(50) NOT NULL UNIQUE,
   senha_hash_usuario VARCHAR(255) NOT NULL, -- sempre armazenar hash (bcrypt/argon2), nunca texto puro
   nivel_acesso_usuario VARCHAR(30) NOT NULL,
   status_usuario VARCHAR(20) DEFAULT 'Ativo',
   ultimo_login_usuario TIMESTAMP,
   data_criacao_usuario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (id_colaborador_usuario) REFERENCES colaborador(id_colaborador),
   CONSTRAINT chk_nivel_acesso_usuario CHECK (nivel_acesso_usuario IN ('Administrador', 'Contador', 'Assistente', 'Cliente')),
   CONSTRAINT chk_status_usuario CHECK (status_usuario IN ('Ativo', 'Inativo', 'Bloqueado'))
);
 
-- 4. Tabela: LOG_AUDITORIA
CREATE TABLE log_auditoria (
   id_log_auditoria BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_usuario_log_auditoria BIGINT, -- nullable: ação automática do sistema não tem usuário
   tabela_afetada_log_auditoria VARCHAR(100) NOT NULL,
   id_registro_afetado_log_auditoria BIGINT NOT NULL,
   tipo_operacao_log_auditoria VARCHAR(20) NOT NULL,
   dados_anteriores_log_auditoria TEXT,
   dados_novos_log_auditoria TEXT,
   ip_origem_log_auditoria VARCHAR(45),
   data_hora_log_auditoria TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (id_usuario_log_auditoria) REFERENCES usuario(id_usuario),
   CONSTRAINT chk_tipo_operacao_log_auditoria CHECK (tipo_operacao_log_auditoria IN ('INSERT', 'UPDATE', 'DELETE'))
);
CREATE INDEX idx_log_auditoria_tabela ON log_auditoria(tabela_afetada_log_auditoria, id_registro_afetado_log_auditoria);
CREATE INDEX idx_log_auditoria_data ON log_auditoria(data_hora_log_auditoria);
 
 
-- ==============================================================================
-- GRUPO 2: EMPRESA
-- ==============================================================================
 
-- 5. Tabela: EMPRESA
CREATE TABLE empresa (
   id_empresa BIGINT AUTO_INCREMENT PRIMARY KEY,
   razao_social_empresa VARCHAR(255) NOT NULL,
   nome_fantasia_empresa VARCHAR(255),
   cnpj_empresa VARCHAR(14) NOT NULL UNIQUE,
   inscricao_estadual_empresa VARCHAR(20),
   inscricao_municipal_empresa VARCHAR(20),
   cnae_principal_empresa VARCHAR(7) NOT NULL,
   regime_tributario_empresa VARCHAR(50) NOT NULL,
   data_abertura_empresa DATE NOT NULL,
   data_cadastro_empresa TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   status_empresa VARCHAR(20) DEFAULT 'Ativo',
   email_empresa VARCHAR(100) NOT NULL,
   telefone_empresa VARCHAR(20) NOT NULL,
   logradouro_empresa VARCHAR(255) NOT NULL,
   numero_empresa VARCHAR(20) NOT NULL,
   complemento_empresa VARCHAR(100),
   bairro_empresa VARCHAR(100) NOT NULL,
   cidade_empresa VARCHAR(100) NOT NULL,
   uf_empresa CHAR(2) NOT NULL,
   cep_empresa VARCHAR(8) NOT NULL,
   capital_social_empresa DECIMAL(15,2) NOT NULL,
   id_colaborador_resp_empresa BIGINT,
   FOREIGN KEY (id_colaborador_resp_empresa) REFERENCES colaborador(id_colaborador),
   CONSTRAINT chk_status_empresa CHECK (status_empresa IN ('Ativo', 'Inativo', 'Suspenso'))
);
CREATE INDEX idx_empresa_cnpj ON empresa(cnpj_empresa);
 
-- 6. Tabela: CONTATO_EMPRESA
CREATE TABLE contato_empresa (
   id_contato_empresa BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_contato_empresa BIGINT NOT NULL,
   nome_contato_empresa VARCHAR(255) NOT NULL,
   cargo_contato_empresa VARCHAR(100),
   email_contato_empresa VARCHAR(100),
   telefone_contato_empresa VARCHAR(20),
   tipo_contato_empresa VARCHAR(30) NOT NULL,
   principal_contato_empresa BOOLEAN DEFAULT FALSE,
   FOREIGN KEY (id_empresa_contato_empresa) REFERENCES empresa(id_empresa),
   CONSTRAINT chk_tipo_contato_empresa CHECK (tipo_contato_empresa IN ('Financeiro', 'Fiscal', 'Societário', 'Geral'))
);
CREATE INDEX idx_contato_empresa_empresa ON contato_empresa(id_empresa_contato_empresa);
