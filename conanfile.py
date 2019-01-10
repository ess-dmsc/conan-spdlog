import os
from conans import ConanFile, CMake, tools


class spdlogConan(ConanFile):
    name = "spdlog"
    src_version = "1.2.1"
    version = "1.2.1-dm1"
    homepage = "https://github.com/ess-dmsc/spdlog"
    license = "BSD 2-Clause"
    url = "https://github.com/ess-dmsc/conan-spdlog"
    description = "spdlog with graylog-logger sink"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    _source_subfolder = "source_subfolder"
    requires = ("fmt/5.2.1@bincrafters/stable", "graylog-logger/1.1.1-dm1@ess-dmsc/stable")
    default_user = "ess-dmsc"
    default_channel = "stable"

    def source(self):
        tools.get("{0}/archive/v1.x.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["SPDLOG_BUILD_EXAMPLES"] = False
        cmake.definitions["SPDLOG_BUILD_TESTING"] = False
        cmake.definitions["SPDLOG_BUILD_BENCH"] = False
        cmake.definitions["SPDLOG_FMT_EXTERNAL"] = True
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        tools.replace_in_file(os.path.join(self.package_folder, "lib", "cmake", "spdlog", "spdlogConfig.cmake"),
                              'add_library(spdlog::spdlog INTERFACE IMPORTED)',
                              'add_library(spdlog::spdlog INTERFACE IMPORTED)\n'
                              'set_target_properties(spdlog::spdlog PROPERTIES\n'
                              'INTERFACE_COMPILE_DEFINITIONS "SPDLOG_FMT_EXTERNAL")')
        self.copy(pattern="LICENSE", dst='licenses', src=self._source_subfolder)

    def package_info(self):
        self.cpp_info.defines.append("SPDLOG_FMT_EXTERNAL")
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

    def package_id(self):
        self.info.header_only()