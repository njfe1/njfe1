#!/bin/bash
 
# This file is accessible as https://install.direct/go.sh
# Original source is located at github.com/v2ray/v2ray-core/release/install-release.sh
 
# If not specify, default meaning of return value:
# : Success
# : System error
# : Application error
# : Network error
 
CUR_VER=""
NEW_VER=""
ARCH=""
VDIS="
ZIPFILE="/tmp/v2ray/v2ray.zip"
V2RAY_RUNNING=
 
CMD_INSTALL=""
CMD_UPDATE=""
SOFTWARE_UPDATED=
 
SYSTEMCTL_CMD=$(command -v systemctl >/dev/null)
SERVICE_CMD=$(command -v service >/dev/null)
 
CHECK=""
FORCE=""
HELP=""
 
#######color code########
RED="31m"      # Error message
GREEN="32m"    # Success message
YELLOW="33m"   # Warning message
BLUE="36m"     # Info message
 
#########################
 ]];do
    key="$1"
    case $key in
        -p|--proxy)
        PROXY="-x ${2}"
        shift # past argument
        ;;
        -h|--help)
        HELP="
        ;;
        -f|--force)
        FORCE="
        ;;
        -c|--check)
        CHECK="
        ;;
        --remove)
        REMOVE="
        ;;
        --version)
        VERSION="$2"
        shift
        ;;
        -l|--local)
        LOCAL="$2"
        LOCAL_INSTALL="
        shift
        ;;
        *)
                # unknown option
        ;;
    esac
    shift # past argument or value
done
 
###############################
colorEcho(){
    COLOR=$
    echo -e "\033[${COLOR}${@:2}\033[0m"
}
 
sysArch(){
    ARCH=$(uname -m)
    if [[ "$ARCH" == "i686" ]] || [[ "$ARCH" == "i386" ]]; then
        VDIS="
    elif [[ "$ARCH" == *"armv7"* ]] || [[ "$ARCH" == "armv6l" ]]; then
        VDIS="arm"
    elif [[ "$ARCH" == *"armv8"* ]] || [[ "$ARCH" == "aarch64" ]]; then
        VDIS="arm64"
    elif [[ "$ARCH" == *"mips64le"* ]]; then
        VDIS="mips64le"
    elif [[ "$ARCH" == *"mips64"* ]]; then
        VDIS="mips64"
    elif [[ "$ARCH" == *"mipsle"* ]]; then
        VDIS="mipsle"
    elif [[ "$ARCH" == *"mips"* ]]; then
        VDIS="mips"
    elif [[ "$ARCH" == *"s390x"* ]]; then
        VDIS="s390x"
    fi
    return
}
 
downloadV2Ray(){
    rm -rf /tmp/v2ray
    mkdir -p /tmp/v2ray
    colorEcho ${BLUE} "Downloading V2Ray."
    DOWNLOAD_LINK="https://github.com/v2ray/v2ray-core/releases/download/${NEW_VER}/v2ray-linux-${VDIS}.zip"
    curl ${PROXY} -L -H "Cache-Control: no-cache" -o ${ZIPFILE} ${DOWNLOAD_LINK}
     ];then
        colorEcho ${RED} "Failed to download! Please check your network or try again."
        return
    fi
    return
}
 
installSoftware(){
    COMPONENT=$
    if [[ -n `command -v $COMPONENT` ]]; then
        return
    fi
 
    getPMT
     ]]; then
        colorEcho ${RED} "The system package manager tool isn't APT or YUM, please install ${COMPONENT} manually."
        return
    fi
     ]]; then
        colorEcho ${BLUE} "Updating software repo"
        $CMD_UPDATE
        SOFTWARE_UPDATED=
    fi
 
    colorEcho ${BLUE} "Installing ${COMPONENT}"
    $CMD_INSTALL $COMPONENT
     ]]; then
        colorEcho ${RED} "Failed to install ${COMPONENT}. Please install it manually."
        return
    fi
    return
}
 
# return : not apt, yum, or zypper
getPMT(){
    if [[ -n `command -v apt-get` ]];then
        CMD_INSTALL="apt-get -y -qq install"
        CMD_UPDATE="apt-get -qq update"
    elif [[ -n `command -v yum` ]]; then
        CMD_INSTALL="yum -y -q install"
        CMD_UPDATE="yum -q makecache"
    elif [[ -n `command -v zypper` ]]; then
        CMD_INSTALL="zypper -y install"
        CMD_UPDATE="zypper ref"
    else
        return
    fi
    return
}
 
extract(){
    colorEcho ${BLUE}"Extracting V2Ray package to /tmp/v2ray."
    mkdir -p /tmp/v2ray
     -d "/tmp/v2ray/"
     ]]; then
        colorEcho ${RED} "Failed to extract V2Ray."
        return
    fi
    return
}
 
# : new V2Ray. : no. : not installed. : check failed. : don't check.
getVersion(){
    if [[ -n "$VERSION" ]]; then
        NEW_VER="$VERSION"
        return
    else
        VER=`/usr/bin/v2ray/v2ray -version >/dev/null`
        RETVAL="$?"
        CUR_VER=` | cut -d " " -f2`
        TAG_URL="https://api.github.com/repos/v2ray/v2ray-core/releases/latest"
        NEW_VER=`curl ${PROXY} -s ${TAG_URL} --connect-timeout | grep 'tag_name' | cut -d\" -f4`
         ]] || [[ $NEW_VER == "" ]]; then
            colorEcho ${RED} "Failed to fetch release information. Please check your network or try again."
            return
         ]];then
            return
        elif [[ "$NEW_VER" != "$CUR_VER" ]];then
            return
        fi
        return
    fi
}
 
stopV2ray(){
    colorEcho ${BLUE} "Shutting down V2Ray service."
    if [[ -n "${SYSTEMCTL_CMD}" ]] || [[ -f "/lib/systemd/system/v2ray.service" ]] || [[ -f "/etc/systemd/system/v2ray.service" ]]; then
        ${SYSTEMCTL_CMD} stop v2ray
    elif [[ -n "${SERVICE_CMD}" ]] || [[ -f "/etc/init.d/v2ray" ]]; then
        ${SERVICE_CMD} v2ray stop
    fi
     ]]; then
        colorEcho ${YELLOW} "Failed to shutdown V2Ray service."
        return
    fi
    return
}
 
startV2ray(){
    if [ -n "${SYSTEMCTL_CMD}" ] && [ -f "/lib/systemd/system/v2ray.service" ]; then
        ${SYSTEMCTL_CMD} start v2ray
    elif [ -n "${SYSTEMCTL_CMD}" ] && [ -f "/etc/systemd/system/v2ray.service" ]; then
        ${SYSTEMCTL_CMD} start v2ray
    elif [ -n "${SERVICE_CMD}" ] && [ -f "/etc/init.d/v2ray" ]; then
        ${SERVICE_CMD} v2ray start
    fi
     ]]; then
        colorEcho ${YELLOW} "Failed to start V2Ray service."
        return
    fi
    return
}
 
copyFile() {
    NAME=$
    ERROR=`>&`
     ]]; then
        colorEcho ${YELLOW} "${ERROR}"
        return
    fi
    return
}
 
makeExecutable() {
    chmod +x "/usr/bin/v2ray/$1"
}
 
installV2Ray(){
    # Install V2Ray binary to /usr/bin/v2ray
    mkdir -p /usr/bin/v2ray
    copyFile v2ray
     ]]; then
        colorEcho ${RED} "Failed to copy V2Ray binary and resources."
        return
    fi
    makeExecutable v2ray
    copyFile v2ctl && makeExecutable v2ctl
    copyFile geoip.dat
    copyFile geosite.dat
 
    # Install V2Ray server config to /etc/v2ray
    if [[ ! -f "/etc/v2ray/config.json" ]]; then
        mkdir -p /etc/v2ray
        mkdir -p /var/log/v2ray
        cp "/tmp/v2ray/v2ray-${NEW_VER}-linux-${VDIS}/vpoint_vmess_freedom.json" "/etc/v2ray/config.json"
         ]]; then
            colorEcho ${YELLOW} "Failed to create V2Ray configuration file. Please create it manually."
            return
        fi
        let PORT=$RANDOM+
        UUID=$(cat /proc/sys/kernel/random/uuid)
 
        sed -i "s/10086/${PORT}/g" "/etc/v2ray/config.json"
        sed -i "s/23ad6b10-8d1a-40f7-8ad0-e3e35cd38297/${UUID}/g" "/etc/v2ray/config.json"
 
        colorEcho ${BLUE} "PORT:${PORT}"
        colorEcho ${BLUE} "UUID:${UUID}"
    fi
    return
}
 
installInitScript(){
    if [[ -n "${SYSTEMCTL_CMD}" ]];then
        if [[ ! -f "/etc/systemd/system/v2ray.service" ]]; then
            if [[ ! -f "/lib/systemd/system/v2ray.service" ]]; then
                cp "/tmp/v2ray/v2ray-${NEW_VER}-linux-${VDIS}/systemd/v2ray.service" "/etc/systemd/system/"
                systemctl enable v2ray.service
            fi
        fi
        return
    elif [[ -n "${SERVICE_CMD}" ]] && [[ ! -f "/etc/init.d/v2ray" ]]; then
        installSoftware "daemon" || return $?
        cp "/tmp/v2ray/v2ray-${NEW_VER}-linux-${VDIS}/systemv/v2ray" "/etc/init.d/v2ray"
        chmod +x "/etc/init.d/v2ray"
        update-rc.d v2ray defaults
    fi
    return
}
 
Help(){
    echo "./install-release.sh [-h] [-c] [--remove] [-p proxy] [-f] [--version vx.y.z] [-l file]"
    echo "  -h, --help            Show help"
    echo "  -p, --proxy           To download through a proxy server, use -p socks5://127.0.0.1:1080 or -p http://127.0.0.1:3128 etc"
    echo "  -f, --force           Force install"
    echo "      --version         Install a particular version, use --version v3.15"
    echo "  -l, --local           Install from a local file"
    echo "      --remove          Remove installed V2Ray"
    echo "  -c, --check           Check for update"
    return
}
 
remove(){
    if [[ -n "${SYSTEMCTL_CMD}" ]] && [[ -f "/etc/systemd/system/v2ray.service" ]];then
        if pgrep "v2ray" > /dev/null ; then
            stopV2ray
        fi
        systemctl disable v2ray.service
        rm -rf "/usr/bin/v2ray" "/etc/systemd/system/v2ray.service"
         ]]; then
            colorEcho ${RED} "Failed to remove V2Ray."
            return
        else
            colorEcho ${GREEN} "Removed V2Ray successfully."
            colorEcho ${BLUE} "If necessary, please remove configuration file and log file manually."
            return
        fi
    elif [[ -n "${SYSTEMCTL_CMD}" ]] && [[ -f "/lib/systemd/system/v2ray.service" ]];then
        if pgrep "v2ray" > /dev/null ; then
            stopV2ray
        fi
        systemctl disable v2ray.service
        rm -rf "/usr/bin/v2ray" "/lib/systemd/system/v2ray.service"
         ]]; then
            colorEcho ${RED} "Failed to remove V2Ray."
            return
        else
            colorEcho ${GREEN} "Removed V2Ray successfully."
            colorEcho ${BLUE} "If necessary, please remove configuration file and log file manually."
            return
        fi
    elif [[ -n "${SERVICE_CMD}" ]] && [[ -f "/etc/init.d/v2ray" ]]; then
        if pgrep "v2ray" > /dev/null ; then
            stopV2ray
        fi
        rm -rf "/usr/bin/v2ray" "/etc/init.d/v2ray"
         ]]; then
            colorEcho ${RED} "Failed to remove V2Ray."
            return
        else
            colorEcho ${GREEN} "Removed V2Ray successfully."
            colorEcho ${BLUE} "If necessary, please remove configuration file and log file manually."
            return
        fi
    else
        colorEcho ${YELLOW} "V2Ray not found."
        return
    fi
}
 
checkUpdate(){
    echo "Checking for update."
    VERSION=""
    getVersion
    RETVAL="$?"
     ]]; then
        colorEcho ${BLUE} "Found new version ${NEW_VER} for V2Ray.(Current version:$CUR_VER)"
     ]]; then
        colorEcho ${BLUE} "No new version. Current version is ${NEW_VER}."
     ]]; then
        colorEcho ${YELLOW} "No V2Ray installed."
        colorEcho ${BLUE} "The newest version for V2Ray is ${NEW_VER}."
    fi
    return
}
 
main(){
    #helping information
    [[ " ]] && Help && return
    [[ " ]] && checkUpdate && return
    [[ " ]] && remove && return
 
    sysArch
    # extract local file
     ]]; then
        echo "Installing V2Ray via local file"
        installSoftware unzip || return $?
        rm -rf /tmp/v2ray
        extract $LOCAL || return $?
        FILEVDIS=`ls /tmp/v2ray |grep v2ray-v |cut -d "-" -f4`
        SYSTEM=`ls /tmp/v2ray |grep v2ray-v |cut -d "-" -f3`
        if [[ ${SYSTEM} != "linux" ]]; then
            colorEcho ${RED} "The local V2Ray can not be installed in linux."
            return
        elif [[ ${FILEVDIS} != ${VDIS} ]]; then
            colorEcho ${RED} "The local V2Ray can not be installed in ${ARCH} system."
            return
        else
            NEW_VER=`ls /tmp/v2ray |grep v2ray-v |cut -d "-" -f2`
        fi
    else
        # download via network and extract
        installSoftware "curl" || return $?
        getVersion
        RETVAL="$?"
         ]] && [[ " ]]; then
            colorEcho ${BLUE} "Latest version ${NEW_VER} is already installed."
            return
         ]]; then
            return
        else
            colorEcho ${BLUE} "Installing V2Ray ${NEW_VER} on ${ARCH}"
            downloadV2Ray || return $?
            installSoftware unzip || return $?
            extract ${ZIPFILE} || return $?
        fi
    fi
    if pgrep "v2ray" > /dev/null ; then
        V2RAY_RUNNING=
        stopV2ray
    fi
    installV2Ray || return $?
    installInitScript || return $?
     ]];then
        colorEcho ${BLUE} "Restarting V2Ray service."
        startV2ray
    fi
    colorEcho ${GREEN} "V2Ray ${NEW_VER} is installed."
    rm -rf /tmp/v2ray
    return
}
 
main