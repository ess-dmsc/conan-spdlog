#include <iostream>
#include <spdlog/spdlog.h>
#include <spdlog/sinks/graylog_sink.h>
#include <memory>
#include <mutex>

int main() {
    auto logger = spdlog::sinks::graylog_sink_mt("graylog_logger", spdlog::level::trace, "0.0.0.0", 12201);
    logger->trace("trace message");
    logger->debug("debug message");
    logger->info("info message");
    logger->critical("critical message");
    return 0;
}
