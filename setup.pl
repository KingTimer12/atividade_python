#!/usr/bin/perl bash
use strict;
use warnings;
use File::Spec;
use Cwd;
use Config;

my $current_dir = getcwd;

# Função para checar e pegar um comando
sub command_exist {
    my ($command) = @_;
    my $path;
    if ($^O eq 'MSWin32') { # Verifica se é win ou não o sistema operacional.
        $path = `where $command 2>NUL`
    } else {
        $path = `which $command 2>/dev/null`;
    }
    chomp $path;
    return $path if $path; # Retorna o caminho do comando se caso existir
    return;
}


sub setup_python {
    my $python = command_exist('py') || command_exist('python') || command_exist('python3');
    if (!$python) {
        die "Python em falta.\n";
    }

    my $venv_path = File::Spec->catdir($current_dir, 'venv');

    unless (-d $venv_path) {
        print "Ambiente virtual em falta.\n";
        print "Criando um ambiente virtual do zero...\n";
        my $create_venv_cmd = "\"$python\" -m venv \"$venv_path\"";
        system($create_venv_cmd) == 0
            or die "Falha ao criar ambiente virtual: $!\n";
        print "Ambiente virtual criado com sucesso.\n";
    }

    print "Ativando ambiente virtual e instalando dep...\n";

    my $activate_venv;
    if ($^O eq 'MSWin32') {
        $activate_venv = File::Spec->catfile($venv_path, 'Scripts', 'activate');
    } else {
        $activate_venv = File::Spec->catfile($venv_path, 'bin', 'activate');
    }

    my $requirements_file = File::Spec->catfile($venv_path, '..', 'requirements.txt');

    my $install_deps_cmd;
    if ($^O eq 'MSWin32') {
        $install_deps_cmd = "cmd /c \"$activate_venv\" && pip install -r \"$requirements_file\"";
    } else {
        $install_deps_cmd = ". \"$activate_venv\" && pip install -r \"$requirements_file\"";
    }

    system($install_deps_cmd) == 0
        or die "Falha ao instalar dep: $!\n";

    print "Tudo foi instalado com sucesso.\n";
}

sub creatdb {
    my $db_dir = File::Spec->catdir($current_dir, 'storage');
    unless (-d $db_dir) {
        print "Armazenamento em falta.\n";
        print "Criando um novo do zero...\n";
        mkdir $db_dir;
        open my $dbFile, ">>", "$db_dir/data.sqlite" or die "Erro ao criar data.sqlite em '$db_dir'"; # Cria o arquivo ou dá erro.
        close $dbFile; # Fecha o arquivo sem nenhuma alteração
    } # Verifica se existe um diretório, caso contrário, criará.
}

setup_python();
creatdb();