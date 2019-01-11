#include <iostream>
#include <spdlog/spdlog.h>
#include <spdlog/sinks/graylog_sink.h>
#include <memory>
#include <mutex>

using my_sink_mt = spdlog::sinks::graylog_sink<std::mutex>;

int main() {
    std::string Host = "localhost";
    auto Sink = std::make_shared<my_sink_mt>(Host, 12201);
    auto GraylogLogger = std::make_shared<spdlog::logger>("graylog", Sink);
    GraylogLogger->warn("test fmt {}", "as well");
    return 0;
}
