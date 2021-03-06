import os
from conans import ConanFile, CMake, tools


class spdlogConan(ConanFile):
    name = "spdlog-graylog"
    libname = "spdlog"
    src_version = "1.5.0"
    version = "1.5.0-dm2"
    homepage = "https://github.com/ess-dmsc/spdlog"
    license = "BSD 2-Clause"
    url = "https://github.com/ess-dmsc/conan-spdlog"
    description = "spdlog with graylog-logger sink"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    _source_subfolder = "source_subfolder"
    exports_sources = ["CMakeLists.txt"]
    requires = ("fmt/6.1.2", "graylog-logger/2.0.3-dm1@ess-dmsc/stable")
    default_user = "ess-dmsc"
    default_channel = "stable"

    def source(self):
        tools.get("{0}/archive/v1.x.tar.gz".format(self.homepage))
        extracted_dir = self.libname + "-1.x"
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["SPDLOG_BUILD_EXAMPLES"] = False
        cmake.definitions["SPDLOG_BUILD_TESTS"] = False
        cmake.definitions["SPDLOG_BUILD_BENCH"] = False
        cmake.definitions["SPDLOG_FMT_EXTERNAL"] = False
        cmake.configure(source_dir=self._source_subfolder, build_dir='.')
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy(pattern="LICENSE", dst='licenses', src=self._source_subfolder)

    def package_info(self):
        self.cpp_info.defines.append("SPDLOG_FMT_EXTERNAL")
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

    def package_id(self):
        self.info.header_only()
