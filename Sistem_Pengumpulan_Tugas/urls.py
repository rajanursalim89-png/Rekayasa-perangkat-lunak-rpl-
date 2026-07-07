"""
URL configuration for Sistem_Pengumpulan_Tugas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from TugasMaster import views

urlpatterns = [

    path('admin/', admin.site.urls),

    # ================= ADMIN =================
    path('data-admin/', views.admin_list),
    path('data-admin/tambah/', views.admin_tambah),
    path('data-admin/<int:id>/', views.admin_detail),
    path('data-admin/<int:id>/edit/', views.admin_edit),
    path('data-admin/<int:id>/hapus/', views.admin_hapus),

    # ================= MAHASISWA =================
    path('mahasiswa/', views.mahasiswa_list),
    path('mahasiswa/tambah/', views.mahasiswa_tambah),
    path('mahasiswa/<int:id>/', views.mahasiswa_detail),
    path('mahasiswa/<int:id>/edit/', views.mahasiswa_edit),
    path('mahasiswa/<int:id>/hapus/', views.mahasiswa_hapus),

    # ================= MATA KULIAH =================
    path('mata-kuliah/', views.matakuliah_list),
    path('mata-kuliah/tambah/', views.matakuliah_tambah),
    path('mata-kuliah/<int:id>/', views.matakuliah_detail),
    path('mata-kuliah/<int:id>/edit/', views.matakuliah_edit),
    path('mata-kuliah/<int:id>/hapus/', views.matakuliah_hapus),

    # ================= TUGAS =================
    path('tugas/', views.tugas_list),
    path('tugas/tambah/', views.tugas_tambah),
    path('tugas/<int:id>/', views.tugas_detail),
    path('tugas/<int:id>/edit/', views.tugas_edit),
    path('tugas/<int:id>/hapus/', views.tugas_hapus),

    # ================= KELAS =================
    path('kelas/', views.kelas_list),
    path('kelas/tambah/', views.kelas_tambah),
    path('kelas/<int:id>/', views.kelas_detail),
    path('kelas/<int:id>/edit/', views.kelas_edit),
    path('kelas/<int:id>/hapus/', views.kelas_hapus),

    # ================= PENGUMPULAN TUGAS =================
    path('pengumpulan/', views.pengumpulan_list),
    path('pengumpulan/tambah/', views.pengumpulan_tambah),
    path('pengumpulan/<int:id>/', views.pengumpulan_detail),
    path('pengumpulan/<int:id>/edit/', views.pengumpulan_edit),
    path('pengumpulan/<int:id>/hapus/', views.pengumpulan_hapus),

    # ================= DETAIL PENGUMPULAN =================
    path('detail-pengumpulan/', views.detailpengumpulan_list),
    path('detail-pengumpulan/tambah/', views.detailpengumpulan_tambah),
    path('detail-pengumpulan/<int:id>/', views.detailpengumpulan_detail),
    path('detail-pengumpulan/<int:id>/edit/', views.detailpengumpulan_edit),
    path('detail-pengumpulan/<int:id>/hapus/', views.detailpengumpulan_hapus),

    # ================= PENILAIAN =================
    path('penilaian/', views.penilaian_list),
    path('penilaian/tambah/', views.penilaian_tambah),
    path('penilaian/<int:id>/', views.penilaian_detail),
    path('penilaian/<int:id>/edit/', views.penilaian_edit),
    path('penilaian/<int:id>/hapus/', views.penilaian_hapus),

    # ================= LAPORAN PENGUMPULAN =================
    path('laporan/', views.laporan_list),
    path('laporan/tambah/', views.laporan_tambah),
    path('laporan/<int:id>/', views.laporan_detail),
    path('laporan/<int:id>/edit/', views.laporan_edit),
    path('laporan/<int:id>/hapus/', views.laporan_hapus),
]
