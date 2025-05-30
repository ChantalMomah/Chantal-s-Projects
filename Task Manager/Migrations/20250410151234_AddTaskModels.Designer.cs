﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Task_Manager.Data;

#nullable disable

namespace Task_Manager.Migrations
{
    [DbContext(typeof(TaskManagerContext))]
    [Migration("20250410151234_AddTaskModels")]
    partial class AddTaskModels
    {
        /// <inheritdoc />
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "8.0.13")
                .HasAnnotation("Relational:MaxIdentifierLength", 64);

            modelBuilder.Entity("TaskItem", b =>
                {
                    b.Property<int>("TaskID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    b.Property<int?>("CategoryID")
                        .HasColumnType("int");

                    b.Property<DateTime>("CreatedDate")
                        .HasColumnType("datetime(6)");

                    b.Property<string>("Description")
                        .IsRequired()
                        .HasMaxLength(500)
                        .HasColumnType("varchar(500)");

                    b.Property<DateTime>("DueDate")
                        .HasColumnType("datetime(6)");

                    b.Property<DateTime>("ModifiedDate")
                        .HasColumnType("datetime(6)");

                    b.Property<string>("Priority")
                        .IsRequired()
                        .HasMaxLength(20)
                        .HasColumnType("varchar(20)");

                    b.Property<string>("Status")
                        .IsRequired()
                        .HasMaxLength(20)
                        .HasColumnType("varchar(20)");

                    b.Property<string>("TaskName")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.Property<string>("Title")
                        .IsRequired()
                        .HasMaxLength(100)
                        .HasColumnType("varchar(100)");

                    b.Property<int>("UserID")
                        .HasColumnType("int");

                    b.HasKey("TaskID");

                    b.HasIndex("CategoryID");

                    b.HasIndex("UserID");

                    b.ToTable("TaskItems");
                });

            modelBuilder.Entity("Task_Manager.Models.TaskCategory", b =>
                {
                    b.Property<int>("CategoryID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    b.Property<string>("CategoryName")
                        .IsRequired()
                        .HasMaxLength(100)
                        .HasColumnType("varchar(100)");

                    b.Property<string>("Color")
                        .IsRequired()
                        .HasMaxLength(20)
                        .HasColumnType("varchar(20)");

                    b.Property<DateTime>("CreatedDate")
                        .HasColumnType("datetime(6)");

                    b.Property<string>("Description")
                        .IsRequired()
                        .HasMaxLength(500)
                        .HasColumnType("varchar(500)");

                    b.Property<int>("UserID")
                        .HasColumnType("int");

                    b.HasKey("CategoryID");

                    b.HasIndex("UserID");

                    b.ToTable("TaskCategories");
                });

            modelBuilder.Entity("Task_Manager.Models.TaskTag", b =>
                {
                    b.Property<int>("TagID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    b.Property<DateTime>("CreatedDate")
                        .HasColumnType("datetime(6)");

                    b.Property<string>("TagName")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.Property<int>("TaskID")
                        .HasColumnType("int");

                    b.Property<int>("UserID")
                        .HasColumnType("int");

                    b.HasKey("TagID");

                    b.HasIndex("TaskID");

                    b.HasIndex("UserID");

                    b.ToTable("TaskTags");
                });

            modelBuilder.Entity("Task_Manager.Models.User", b =>
                {
                    b.Property<int>("UserID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    b.Property<DateTime>("DateCreated")
                        .HasColumnType("datetime(6)");

                    b.Property<DateTime?>("LastLogin")
                        .HasColumnType("datetime(6)");

                    b.Property<string>("Name")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.Property<string>("UserEmail")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.Property<string>("UserName")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.Property<string>("UserPassword")
                        .IsRequired()
                        .HasColumnType("longtext");

                    b.HasKey("UserID");

                    b.ToTable("Users");
                });

            modelBuilder.Entity("TaskItem", b =>
                {
                    b.HasOne("Task_Manager.Models.TaskCategory", "Category")
                        .WithMany("TaskItems")
                        .HasForeignKey("CategoryID")
                        .OnDelete(DeleteBehavior.SetNull);

                    b.HasOne("Task_Manager.Models.User", "User")
                        .WithMany("TaskItems")
                        .HasForeignKey("UserID")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Category");

                    b.Navigation("User");
                });

            modelBuilder.Entity("Task_Manager.Models.TaskCategory", b =>
                {
                    b.HasOne("Task_Manager.Models.User", "User")
                        .WithMany("Categories")
                        .HasForeignKey("UserID")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("User");
                });

            modelBuilder.Entity("Task_Manager.Models.TaskTag", b =>
                {
                    b.HasOne("TaskItem", "TaskItem")
                        .WithMany("TaskTags")
                        .HasForeignKey("TaskID")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("Task_Manager.Models.User", "User")
                        .WithMany("TaskTags")
                        .HasForeignKey("UserID")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("TaskItem");

                    b.Navigation("User");
                });

            modelBuilder.Entity("TaskItem", b =>
                {
                    b.Navigation("TaskTags");
                });

            modelBuilder.Entity("Task_Manager.Models.TaskCategory", b =>
                {
                    b.Navigation("TaskItems");
                });

            modelBuilder.Entity("Task_Manager.Models.User", b =>
                {
                    b.Navigation("Categories");

                    b.Navigation("TaskItems");

                    b.Navigation("TaskTags");
                });
#pragma warning restore 612, 618
        }
    }
}
