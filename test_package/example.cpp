#include <iostream>
#include <spdlog/spdlog.h>
#include <spdlog/sinks/graylog_sink.h>

int main() {
    auto graylog_logger = std::make_shared<spdlog::sinks::graylog_sink>("", 0);
    graylog_logger->warn("4{}", 2);
}