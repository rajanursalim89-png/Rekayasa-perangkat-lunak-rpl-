from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mahasiswa, Tugas

# Create your views here.

# ==========================
# ADMIN
# ==========================
def admin_list(request):
    return HttpResponse("Halaman Data Admin")

def admin_tambah(request):
    return HttpResponse("Halaman Tambah Admin")

def admin_detail(request, id):
    return HttpResponse(f"Detail Admin {id}")

def admin_edit(request, id):
    return HttpResponse(f"Edit Admin {id}")

def admin_hapus(request, id):
    return HttpResponse(f"Hapus Admin {id}")


# ==========================
# MAHASISWA
# ==========================
def mahasiswa_list(request):
    return HttpResponse("Halaman Data Mahasiswa")

def mahasiswa_tambah(request):
    return HttpResponse("Tambah Mahasiswa")

def mahasiswa_detail(request, id):
    return HttpResponse(f"Detail Mahasiswa {id}")

def mahasiswa_edit(request, id):
    return HttpResponse(f"Edit Mahasiswa {id}")

def mahasiswa_hapus(request, id):
    return HttpResponse(f"Hapus Mahasiswa {id}")


# ==========================
# MATA KULIAH
# ==========================
def matakuliah_list(request):
    return HttpResponse("Data Mata Kuliah")

def matakuliah_tambah(request):
    return HttpResponse("Tambah Mata Kuliah")

def matakuliah_detail(request, id):
    return HttpResponse(f"Detail Mata Kuliah {id}")

def matakuliah_edit(request, id):
    return HttpResponse(f"Edit Mata Kuliah {id}")

def matakuliah_hapus(request, id):
    return HttpResponse(f"Hapus Mata Kuliah {id}")


# ==========================
# TUGAS
# (terhubung ke database & template, contoh CRUD yang sudah berfungsi)
# ==========================
def tugas_list(request):
    tugas = Tugas.objects.all()
    return render(request, 'tugas/list.html', {'tugas': tugas})

def tugas_tambah(request):
    if request.method == 'POST':
        Tugas.objects.create(
            judul=request.POST.get('judul'),
            mata_kuliah=request.POST.get('mata_kuliah'),
            deadline=request.POST.get('deadline'),
            status=request.POST.get('status'),
        )
        return redirect('/tugas/')
    return render(request, 'tugas/tambah.html')

def tugas_detail(request, id):
    tugas = get_object_or_404(Tugas, id=id)
    return render(request, 'tugas/detail.html', {'tugas': tugas})

def tugas_edit(request, id):
    tugas = get_object_or_404(Tugas, id=id)
    if request.method == 'POST':
        tugas.judul = request.POST.get('judul')
        tugas.mata_kuliah = request.POST.get('mata_kuliah')
        tugas.deadline = request.POST.get('deadline')
        tugas.status = request.POST.get('status')
        tugas.save()
        return redirect('/tugas/')
    return render(request, 'tugas/edit.html', {'tugas': tugas})

def tugas_hapus(request, id):
    tugas = get_object_or_404(Tugas, id=id)
    tugas.delete()
    return redirect('/tugas/')


# ==========================
# KELAS
# ==========================
def kelas_list(request):
    return HttpResponse("Data Kelas")

def kelas_tambah(request):
    return HttpResponse("Tambah Kelas")

def kelas_detail(request, id):
    return HttpResponse(f"Detail Kelas {id}")

def kelas_edit(request, id):
    return HttpResponse(f"Edit Kelas {id}")

def kelas_hapus(request, id):
    return HttpResponse(f"Hapus Kelas {id}")


# ==========================
# PENGUMPULAN TUGAS
# ==========================
def pengumpulan_list(request):
    return HttpResponse("Data Pengumpulan Tugas")

def pengumpulan_tambah(request):
    return HttpResponse("Tambah Pengumpulan Tugas")

def pengumpulan_detail(request, id):
    return HttpResponse(f"Detail Pengumpulan Tugas {id}")

def pengumpulan_edit(request, id):
    return HttpResponse(f"Edit Pengumpulan Tugas {id}")

def pengumpulan_hapus(request, id):
    return HttpResponse(f"Hapus Pengumpulan Tugas {id}")


# ==========================
# DETAIL PENGUMPULAN
# ==========================
def detailpengumpulan_list(request):
    return HttpResponse("Data Detail Pengumpulan")

def detailpengumpulan_tambah(request):
    return HttpResponse("Tambah Detail Pengumpulan")

def detailpengumpulan_detail(request, id):
    return HttpResponse(f"Detail Detail Pengumpulan {id}")

def detailpengumpulan_edit(request, id):
    return HttpResponse(f"Edit Detail Pengumpulan {id}")

def detailpengumpulan_hapus(request, id):
    return HttpResponse(f"Hapus Detail Pengumpulan {id}")


# ==========================
# PENILAIAN
# ==========================
def penilaian_list(request):
    return HttpResponse("Data Penilaian")

def penilaian_tambah(request):
    return HttpResponse("Tambah Penilaian")

def penilaian_detail(request, id):
    return HttpResponse(f"Detail Penilaian {id}")

def penilaian_edit(request, id):
    return HttpResponse(f"Edit Penilaian {id}")

def penilaian_hapus(request, id):
    return HttpResponse(f"Hapus Penilaian {id}")


# ==========================
# LAPORAN PENGUMPULAN
# ==========================
def laporan_list(request):
    return HttpResponse("Data Laporan Pengumpulan")

def laporan_tambah(request):
    return HttpResponse("Tambah Laporan")

def laporan_detail(request, id):
    return HttpResponse(f"Detail Laporan {id}")

def laporan_edit(request, id):
    return HttpResponse(f"Edit Laporan {id}")

def laporan_hapus(request, id):
    return HttpResponse(f"Hapus Laporan {id}")
