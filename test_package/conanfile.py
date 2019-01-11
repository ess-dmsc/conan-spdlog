from conans import ConanFile, CMake
import os


class spdlogTestConan(ConanFile):
    requires = ("cmake_installer/3.10.0@conan/stable","fmt/5.2.1@bincrafters/stable", "graylog-logger/1.1.1-dm1@ess"
                                                                                      "-dmsc/stable")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package".
        cmake.configure(source_dir=self.source_folder, build_dir="./")
        cmake.build()

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
